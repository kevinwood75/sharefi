FROM python:3.7-alpine
MAINTAINER woodez.org

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /sharefi
WORKDIR /sharefi
COPY ./sharefi/ /sharefi

RUN adduser -u 5001 -D kwood    
USER kwood