.PHONY: install test lint format run clean

install:
	pip install -e ".[dev]"

test:
	pytest --cov=bell

lint:
	ruff check .

format:
	ruff format . && ruff check --fix .

run:
	bell-lab --shots 8192 --visibility 0.9 --seed 7

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache .coverage htmlcov
