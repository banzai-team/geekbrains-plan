
FROM python:3.11-slim as base

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential gcc-11 g++-11 clang

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # env
    PATH="/opt/venv/bin:${PATH}"

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

FROM base

COPY ./prisma ./prisma
# RUN prisma init --schema ./prisma/prisma.schema
RUN prisma generate --schema ./prisma/prisma.schema

COPY ./app ./app/
