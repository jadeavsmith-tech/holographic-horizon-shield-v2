.PHONY: test-shield

test-shield:
	pip install pytest pytest-asyncio
	pip install --no-cache-dir torch transformers --index-url https://pytorch.org
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	PYTHONPATH=.:src:src/holographic_horizon_shield pytest test_shield.py
