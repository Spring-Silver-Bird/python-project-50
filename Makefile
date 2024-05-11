install:
	poetry install

gendiff-help:
	poetry run gendiff -h

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

lint:
	poetry run flake8 gendiff



