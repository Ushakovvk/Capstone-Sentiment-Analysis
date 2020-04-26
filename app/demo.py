__author__ = 'Ushakov Vadim'
from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request

app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")
print((time.time() - start_time, "seconds"))


@app.route("/sentiment_analysis/", methods=["POST", "GET"])
def index_page(text="Удобное управление, широкая нижняя полка на дверце. Работает тихо. После включения охладился до нужной температуры достаточно быстро.",
               prediction_message="Положительный отзыв",
               prediction_color="success"):
    if request.method == "POST":
        text = request.form["text"]
        logfile = open("ydf_demo_logs.txt", "a", "utf-8")
        print(text)
        print("<response>", file=logfile)
        print(text, file=logfile)
        prediction_color, prediction_message = classifier.get_prediction_message(text)
        print(prediction_message)
        print(prediction_message, file=logfile)
        print("</response>", file=logfile)
        logfile.close()

    return render_template('index.html', text=text, prediction_color=prediction_color,
                           prediction_message=prediction_message)


if __name__ == "__main__":
    app.run()
