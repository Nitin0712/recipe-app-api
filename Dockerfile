FROM python:3.5-alpine
MAINTAINER nitin vishwakarma
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user