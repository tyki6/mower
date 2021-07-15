install-dev:
	pip install -r dev-requirements.txt
lint:
	pre-commit run --all-files
docstr:
	docstr-coverage rawsec_cli tests --skipinit --failunder 95
tox:
	pip install tox tox-gh-actions
	tox
test:
	coverage run --branch -p -m pytest --capture=sys
coverage:
	coverage combine | true && coverage report -m
clean:
	rm -rf .tox .pytest_cache build  dist coverage_html_report   dumpSyntax .coverage .coverage.* .rnd
help:
	@echo "make install-dev       Install dev requirements."
	@echo "make lint              Run Lint."
	@echo "make docstr            Run docstr report."
	@echo "make tox               Run Unit test tox."
	@echo "make test              Run Unit test."
	@echo "make coverage          Show coverage report."
	@echo "make clean             Clean Your project.Delete useless file."
	@echo "make help              Show this help message."
