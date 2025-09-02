# Makefile for btre project (local, sem Docker)

# Variables
PYTHON = python manage.py

.PHONY: all runserver migrations migrate superuser test deploy clean lint seed deps lint-fix fresh-db

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

seed:
	@echo "Seeding the database..."
	$(PYTHON) seed_listings

test:
	@echo "Running tests..."
	$(PYTHON) test

clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

lint:
	@echo "Linting the code..."
	python -m pylint --rcfile=.pylintrc **/*.py

lint-fix:
	@echo "Fixing linting issues..."
	autopep8 --in-place --recursive .

format:
	@echo "Auto-formatting code..."
	python -m isort .
	python -m black .
	python -m autopep8 --in-place --recursive .

deps:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

fresh-db:
	@echo "Resetting the database..."
	rm -f db.sqlite3
	$(MAKE) migrate
	$(MAKE) seed

deploy:
	@echo "Deploying the application..."
	# Add your deployment commands here
