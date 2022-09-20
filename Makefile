all: setup install test

setup:
	python3 -m virtualenv venv;

install:
	. venv/bin/activate && pip install -r requirements.txt
	pre-commit install

test:
	. venv/bin/activate && python -m unittest tests.test_cli