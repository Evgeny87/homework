FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN pip install --upgrade pip && \
    pip install poetry==1.3.1

RUN poetry config virtualenvs.create false --local

COPY poetry.lock /app/poetry.lock
COPY pyproject.toml /app/pyproject.toml

COPY . /app