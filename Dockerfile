# docker build . -t flask-api
FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get install -y --no-install-recommends \
    build-essential wget curl

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY . .

EXPOSE 5000
CMD [ "python", "flaskapi.py" ]