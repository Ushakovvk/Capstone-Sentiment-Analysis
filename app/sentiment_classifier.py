# -*- coding: utf-8 -*-
__author__ = 'Ushakov Vadim'
import pickle


class SentimentClassifier(object):
    def __init__(self):
        with open('pipeline.pkl', 'rb') as f:
            self.model = pickle.load(f)
        self.classes_dict = {0: ['danger', 'Отрицательный отзыв'],
                            1: ['success', 'Положительный отзыв'],
                            -1: ['warning', 'Ошибка']}

    def predict_text(self, text):
        try:
            return self.model.predict([text])[0]
        except:
            print('prediction error')
            return -1

    def predict_list(self, list_of_texts):
        try:
            return self.model.predict([list_of_texts])
        except:
            print('prediction error')
            return None

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction
        return self.classes_dict[class_prediction]
