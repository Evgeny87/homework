# собрать билд докера командой docker build . -t var-app
# запустить докер контейнер командой docker run var-app

FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip && \
    pip install poetry==1.3.1

RUN poetry config virtualenvs.create false --local
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --only main --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port=8000
