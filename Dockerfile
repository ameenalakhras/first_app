FROM python:3.7-alpine3.10
MAINTAINER amin app developer

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# next lines in 2. Add postgres support to Dockerfile.mp4
RUN apk add --update --no-cache postgresql-client
# install postgres dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
