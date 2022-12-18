FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/api

RUN pip install --upgrade pip && \
    pip install poetry==1.3.1

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . .

CMD uvicorn main:app --host 0.0.0.0