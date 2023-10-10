FROM python:3.10-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --without dev

COPY . .
CMD ["python3", "bitwise/__main__.py"]