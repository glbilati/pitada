.PHONY: install up down run migrate lint format typecheck test check openapi

install:
	python3 -m venv .venv
	.venv/bin/pip install -e ".[dev]"

up:
	docker compose up -d db

down:
	docker compose down

run:
	.venv/bin/uvicorn app.main:app --reload --port 8000

migrate:
	.venv/bin/alembic upgrade head

lint:
	.venv/bin/ruff check .

format:
	.venv/bin/ruff format .
	.venv/bin/ruff check --fix .

typecheck:
	.venv/bin/mypy app

test:
	.venv/bin/pytest

# O mesmo que o CI roda. Passou aqui, passa la.
check: lint typecheck test

openapi:
	.venv/bin/python -c "import json; from app.main import app; print(json.dumps(app.openapi(), indent=2, ensure_ascii=False, sort_keys=True))" > docs/openapi.json
