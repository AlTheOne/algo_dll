#!make
.DEFAULT_GOAL := dc-test

# Makefile target args
args = $(filter-out $@,$(MAKECMDGOALS))

# Command shortcuts
mypy = poetry run mypy ./src
flake = poetry run flake8 ./src ./tests
isort = poetry run isort src tests
pytest = poetry run pytest


.PHONY: format
format:
	$(isort)


.PHONY: lint
dc-lint:
	docker run --rm -i -v $(shell pwd)/.hadolint.yaml:/.config/hadolint.yaml hadolint/hadolint < Dockerfile


.PHONY: lint
lint: dc-lint
	$(flake)
	$(isort) --check-only
	$(mypy)


.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf dist *.egg-info
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf artefacts
	rm -f .coverage
	rm -f .coverage.*
	rm -rf artefacts/{htmlcov,test_report.xml}
	rm -rf .hypothesis
