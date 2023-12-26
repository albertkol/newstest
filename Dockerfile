FROM python:3.11-slim-bookworm

RUN pip install poetry==1.7.1

WORKDIR /app

COPY pyproject.toml poetry.lock README.md scripts.py ./
COPY newscorp ./newscorp
COPY tests ./tests

RUN poetry install

ENTRYPOINT []
