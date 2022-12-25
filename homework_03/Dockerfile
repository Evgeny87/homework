FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install poetry==1.3.1

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./

RUN poetry install --only main --no-interaction --no-dev --no-ansi

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port=8000
