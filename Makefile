.PHONY: test-shield
test-shield:
	@printf "pip install pytest pytest-asyncio torch transformers --index-url https://pytorch.org\npip install -r requirements.txt\nPYTHONPATH=.:src:src/holographic_horizon_shield pytest test_shield.py\n" > run.sh && bash run.sh
