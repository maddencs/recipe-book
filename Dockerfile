FROM python:3.13-slim

RUN apt-get -y update \
    && apt-get -y upgrade

COPY . .

RUN pip install -r requirements.txt

WORKDIR /app
