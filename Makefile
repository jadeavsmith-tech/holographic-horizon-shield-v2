# Holographic Horizon Shield v2 - Makefile

.PHONY: help install dev test lint format clean docker

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install -e .

dev: ## Install with development dependencies
	pip install -e .[dev]

test: ## Run tests with coverage
	pytest --cov=holographic_horizon_shield --cov-report=term-missing

lint: ## Run linter
	ruff check .
	black --check .

format: ## Auto-format code
	black .
	ruff check --fix .

clean: ## Clean build artifacts
	rm -rf __pycache__ *.pyc *.pyo .pytest_cache/ .coverage htmlcov/ build/ dist/ *.egg-info/

docker: ## Build Docker image
	docker build -t holographic-horizon-shield .

run: ## Run the Streamlit app
	streamlit run shield_v2_dashboard.py
  
make help      # See all commands
make dev
make test
make format  
