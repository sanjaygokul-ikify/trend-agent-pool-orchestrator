init: venv requirements
debuild: fmt lint test

venv:requirements: python3 -m venv venv
	pip install -r requirements.txt
doc:
	pip install -r docs/requirements.txt
	docsite build
test:
	pytest tests/
lint:
	pylint agent_pool/
fmt:
	black agent_pool/ tests/
ci:
	docker build -t aport-ci .
	docker compose up
deploy:
	sk build
	sk publish