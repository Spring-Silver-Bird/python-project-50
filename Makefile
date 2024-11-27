install:
	poetry install

gendiff-help:
	poetry run gendiff -h

build:
	poetry build

package-install:
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml
	poetry run coverage report

lint:
	poetry run flake8
