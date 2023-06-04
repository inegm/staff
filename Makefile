TOP_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
.PHONY: tests
.SILENT: checks black isort mypy ruff pylint tests build release package

checks: black isort mypy ruff pylint

black:
	echo "- Running black (in check mode) ..."
	black --check src/staff

black-fix:
	echo "- Running black (in fix mode) ..."
	black src/staff

isort:
	echo "- Running isort (in check mode) ..."
	isort --check src/staff

isort-fix:
	echo "- Running isort (in fix mode) ..."
	isort src/staff

mypy:
	echo "- Running mypy ..."
	mypy --show-error-codes --check-untyped-defs src/staff

ruff:
	echo "- Running ruff ..."
	ruff src/staff

pylint:
	echo "- Running pylint ..."
	pylint --errors-only --output-format colorized src/staff

tests:
	echo "- Running doctests ..."
	pytest -c pyproject.toml --maxfail 1 --cov --doctest-modules src/staff/
	echo "- Running unit-tests ..."
	pytest -c pyproject.toml --maxfail 1 --cov

build: checks tests package

release: checks tests package

package:
	echo "- Building distribution ..."
	python -m build .
