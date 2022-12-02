FROM python:3.7.3-alpine3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml /code/

RUN poetry install --no-dev

COPY . /code/
