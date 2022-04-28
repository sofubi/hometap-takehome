FLASK_APP = src/app.py
FLASK := FLASK_APP=$(FLASK_APP) poetry run flask 
POETRY := $(shell command -v poetry 2> /dev/null)

init:
ifndef POETRY
	$(error "Poetry must be installed. Please run >pip install poetry")
endif
	poetry install
	poetry shell

.PHONY: run
run:
	$(FLASK) run

lint:
	poetry run flake8 src/

format:
	poetry run black .

clean: format lint

test:
	poetry run pytest
