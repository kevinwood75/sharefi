FROM python:3.7-alpine
MAINTAINER woodez.org

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /sharefi
WORKDIR /sharefi
COPY ./sharefi/ /sharefi

RUN adduser -u 5001 -D kwood    
USER kwood