
# Makefile for btre project

# Variables
PYTHON = docker-compose exec web python manage.py

.PHONY: all runserver migrations migrate superuser test deploy clean lint

all: runserver

runserver:
	@echo "Starting Django development server..."
	$(PYTHON) runserver 0.0.0.0:8000

migrations:
	@echo "Creating database migrations..."
	$(PYTHON) makemigrations

migrate:
	@echo "Applying database migrations..."
	$(PYTHON) migrate

superuser:
	@echo "Creating a superuser..."
	$(PYTHON) createsuperuser

test:
	@echo "Running tests..."
	$(PYTHON) test

clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

lint:
	@echo "Linting the code..."
	# Assuming pylint is installed in the container
	docker-compose exec web pylint **/*.py
