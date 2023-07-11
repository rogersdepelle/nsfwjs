FROM python:3.11.4-slim

WORKDIR /webapp/

ARG MODE
ENV MODE $MODE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="America/New_York"

COPY ./webapp/requirements/ /webapp/

RUN pip install --upgrade pip

RUN if [ "$MODE" = "production" ]; then pip install -r main.txt; else pip install -r dev.txt; fi

COPY . /webapp/
