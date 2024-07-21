FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main_score.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
