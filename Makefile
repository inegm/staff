TOP_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
.PHONY: tests
.SILENT: checks black isort mypy mypy-report ruff pylint tests tests-report build release package publish

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

mypy-report:
	echo "- Running mypy and generating coverage report..."
	mypy --html-report docs/cov/mypy --show-error-codes --check-untyped-defs src/staff

ruff:
	echo "- Running ruff ..."
	ruff src/staff

pylint:
	echo "- Running pylint ..."
	pylint --errors-only --output-format colorized src/staff

tests:
	echo "- Running doctests ..."
	pytest -c pyproject.toml --maxfail 1 -vvv --cov --doctest-modules src/staff/
	echo "- Running unit-tests ..."
	pytest -c pyproject.toml --maxfail 1 -vvv --cov

tests-report:
	echo "- Running unit-tests and generating coverage report..."
	pytest -c pyproject.toml --maxfail 1 --cov -vvv --cov-report html:docs/cov/tests --cov-report term --ignore tests

build: checks tests package

release: checks tests package publish

package:
	echo "- Building distribution ..."
	python -m build .

publish:
	echo "- Publishing distribution to PyPI ..."
	python -m twine upload -u $(PYPI_U) -p $(PYPI_P) dist/*
