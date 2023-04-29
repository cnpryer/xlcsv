.PHONY: help clean lint fmt mt-check test pre-commit bench lint-type

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  .venv			    create venv and install dependencies"
	@echo "  clean				remove cleanable files"
	@echo "  lint				run linter"
	@echo "  lint-type			run type-checker"
	@echo "  fmt				run formaters"
	@echo "  fmt-check			run formatting check"
	@echo "  test				run all tests"
	@echo "  pre-commit			run pre-commit standardization"
	@echo "  bench				run tests/bench/*"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."
	
clean:
	-@rm -rf .venv
	-@rm -fr `find . -name __pycache__`
	-@rm -rf .pytest_cache
	-@rm -rf .mypy_cache
	-@rm -rf .ruff_cache

lint: .venv
	@rye run ruff check .

lint-type: .venv
	@rye run mypy src tests

fmt: .venv lint
	@ruff check --select I --fix .
	@rye run black .

fmt-check: .venv
	@rye run ruff check --select I .
	@rye run black . --check

test: .venv
	@rye run pytest

pre-commit: test fmt-check lint lint-type

bench:
	@rye run python tests/bench/excel_io.py