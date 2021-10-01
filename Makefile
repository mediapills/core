.PHONY: help

help:
	@echo "  help       to show this help"
	@echo "  build      to build python package"
	@echo "  coverage   to source code coverage check"
	@echo "  linter     to static code analysis"
	@echo "  mypy       to static type checker"
	@echo "  pre-commit to source code validation"
	@echo "  test       to tests running"
	@echo "  validate   to source code validation"

.PHONY: build
build:
	tox -e build

.PHONY: coverage
coverage:
	tox -e coverage

.PHONY: linter
linter:
	tox -e linter

.PHONY: mypy
mypy:
	tox -e mypy

.PHONY: pre-commit
pre-commit:
	tox -e pre-commit

.PHONY: test
test:
	tox

.PHONY: validate
validate:
	tox -e pre-commit
	tox -e linter
	tox -e mypy
