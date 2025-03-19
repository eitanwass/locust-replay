POETRY := poetry

install:
	$(POETRY) install
	$(POETRY) run pip install -e .

test:
	$(POETRY) run pytest -vvv tests/
