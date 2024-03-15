FROM python:3.9.7-slim-buster

WORKDIR /app

RUN pip3 install Flask psutil

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask","run"]