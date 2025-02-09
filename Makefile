install:
	uv install

gendiff-help:
	uv run gendiff -h

build:
	uv build

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov --cov-report xml:coverage.xml

lint:
	uv run ruff check gendiff

.PHONY: install test lint selfcheck check build