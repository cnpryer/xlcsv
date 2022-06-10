ACTIVATE = source venv/bin/activate &&

.PHONY: help clean lint fmt mt-check test pre-commit bench

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  venv				create venv and install dependencies"
	@echo "  clean				remove cleanable files"
	@echo "  lint				run linters"
	@echo "  fmt				run formaters"
	@echo "  fmt-check			run formatting check"
	@echo "  test				run all tests"
	@echo "  pre-commit			run pre-commit standardization"
	@echo "  bench				run tests/bench/*"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

venv:
	@python -m venv venv
	@$(ACTIVATE) poetry install \
		&& pre-commit install

clean:
	-@rm -rf venv
	-@rm -fr `find . -name __pycache__`
	-@rm -rf .pytest_cache
	-@rm -rf .mypy_cache

lint: venv
	@$(ACTIVATE) poetry run flake8 \
		xlcsv \
		tests

fmt: venv
	@$(ACTIVATE) poetry run isort . \
		&& poetry run black .

fmt-check: venv
	@$(ACTIVATE) poetry run isort . --check \
		&& poetry run black . --check

test: venv
	@$(ACTIVATE) poetry run pytest

pre-commit: test fmt lint
	@$(ACTIVATE) poetry run mypy \
		xlcsv \
		tests

bench:
	@$(ACTIVATE) poetry run python tests/bench/excel_io.py