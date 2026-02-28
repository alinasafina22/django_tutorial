FROM python:3.13

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY . .

ENV PYTHONPATH=/app/djangotutorial

CMD ["poetry", "run", "gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
