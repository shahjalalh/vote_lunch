FROM python:3.8.12-slim-buster

LABEL maintainer="shahjalal.tipu@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get -y install gnupg2 wget gcc libc-dev
# RUN apt-get -y install postgresql-client
# RUN apt-get -y install postgresql-client-12

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN useradd user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

USER user