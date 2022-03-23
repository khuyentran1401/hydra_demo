install: 
	@echo "Installing..."
	poetry install

activate:
	@echo "Activating virtual environment"
	poetry shell

pull_data:
	@echo "Pulling data..."
	poetry run dvc pull

setup: activate install pull_data


	
