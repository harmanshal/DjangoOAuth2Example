FROM python:3.10.4-alpine

WORKDIR /usr/src/client

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/client/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .
