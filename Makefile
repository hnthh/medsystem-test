manage = poetry run python manage.py

build:
	docker build --build-arg pyversion=3.11 --tag optics .

db:
	dropdb --if-exists --host 127.0.0.1 --port 5432 --username postgres postgres
	createdb --host 127.0.0.1 --port 5432 --username postgres postgres

	$(manage) migrate

check:
	$(manage) makemigrations --check --no-input --dry-run
	$(manage) check

	poetry run ruff format --check .
	poetry run ruff check .
	poetry run toml-sort pyproject.toml --check

fmt:
	poetry run ruff format .
	poetry run ruff check . --fix --unsafe-fixes
	poetry run toml-sort pyproject.toml

mr: fmt check test

run:
	$(manage) migrate
	$(manage) runserver

test:
	poetry run pytest --create-db
	poetry run pytest --dead-fixtures
