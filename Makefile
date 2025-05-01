#  Makefile for common development tasks

#  Set up the virtual environment
venv:
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt

#  Run the Flask application
run:
	source ./.venv/bin/activate; export PYTHONPATH=$(shell python -c 'import sys; from pathlib import Path; print(Path(".").resolve())'); flask --app src/app.py run --host=0.0.0.0 --port=5000 --debug --cert=cert.pem --key=key.pem

# Run tests
test:
	source ./.venv/bin/activate; export PYTHONPATH=$(shell python -c 'import sys; from pathlib import Path; print(Path(".").resolve())'); pytest -v tests/

#  Format code with black
format:
	source ./.venv/bin/activate; export PYTHONPATH=$(shell python -c 'import sys; from pathlib import Path; print(Path(".").resolve())'); black src tests

#  Run flake8 for linting
lint:
	source ./.venv/bin/activate; export PYTHONPATH=$(shell python -c 'import sys; from pathlib import Path; print(Path(".").resolve())'); flake8 src tests

#  Apply migrations
migrate:
	flask db upgrade

#  Create migrations
migrations:
	flask db migrate
