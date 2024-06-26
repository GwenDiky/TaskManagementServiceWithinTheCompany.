FROM python:3.11.9-alpine3.2

ENV PYTHONDONTWRITEBYTECODE 1 \
ENV PYTHONBUFFERED 1

WORKDIR /app

RUN pip install poetry
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
