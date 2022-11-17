FROM python:latest

LABEL maintainer="webapp"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./webapp /app

WORKDIR /app

RUN ls
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
