# Makefile for Sapphire
configure:
	@echo "Configuring Environment..."
	@export PYTHONPATH=$PYTHONPATH:$(pwd)
	@echo "Done configuring environment."

lint:
	@echo "Linting Sapphire..."
	@curl https://get.trunk.io -fsSL | bash
	@trunk fmt --all
	@echo "Done linting Sapphire."

check:
	@echo "Checking Sapphire code quality"
	@trunk check
	@echo "Done checking Sapphire code quality"
download:
	@echo "Downloading dependencies..."
	@pip install -r requirements.txt
	@echo "Dependencies installed."
test:
	@echo "Running tests..."
	@python -m unittest discover 
	@echo "Done running tests."

run:
	@echo "Starting project..."
	@python -m spacy download en_core_web_sm
	@python sapphire.py
	@echo "Done running."
