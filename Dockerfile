FROM continuumio/miniconda3
COPY /app /app
WORKDIR /app
RUN conda install -c conda-forge flask scikit-learn && pip install gunicorn
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "demo:app"]
