# Makefile for rs-sapphire
configure:
	@echo "Configuring Environment..."
	@export PYTHONPATH=$PYTHONPATH:$(pwd)
	@echo "Done configuring environment."

lint:
	@echo "Linting Sapphire..."
	@curl https://get.trunk.io -fsSL | bash
	@trunk fmt --all
	@cargo clippy
	@echo "Done linting Sapphire."

check:
	@echo "Checking Sapphire code quality"
	@trunk check
	@echo "Done checking Sapphire code quality"
download:
	@echo "Downloading dependencies..."
	@pip install -r requirements.txt
	@echo "Dependencies installed."


run_server:
	@echo "Starting server..."
	@python python/py_sapphire.py
run_main:
	@echo "Starting server..."
	@echo "Start Project..."
	@cargo run
	@echo "Done running"
