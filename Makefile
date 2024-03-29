image_name="py_service:1"

build-image:
	docker build -t ${image_name} .

lint:
	@autoflake --recursive --in-place --remove-unused-variables --remove-all-unused-imports --exclude app/help/shortcuts.py app
	@black .
	@isort .

test:
	@pytest -s tests/*
