FROM ./uwsgi-nginx-flask:python3.10

RUN pip install --upgrade pip && \
    pip install poetry==1.3.1

RUN poetry config virtualenvs.create false --local
COPY poetry.lock .
COPY pyproject.toml .

COPY . /app