# Makefile for Sapphire
configure:
	@echo "Configuring Environment..."
	@export PYTHONPATH=$PYTHONPATH:$(pwd)
	@echo "Done configuring environment."

lint:
	@echo "Linting Sapphire..."
	@trunk fmt --all
	@echo "Done linting Sapphire."

check:
	@echo "Checking Sapphire code quality"
	@trunk check
	@echo "Done checking Sapphire code quality"

test:
	@echo "Running tests..."
	@python -m unittest discover 
	@echo "Done running tests."
run:
	@echo "Starting project..."
	@python -m spacy download en_core_web_sm
	@python sapphire.py
	@echo "Done running."
