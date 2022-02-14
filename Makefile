image_name="py_service:2"

deps:
	pipenv lock -r > requirements.txt

build-image:
	docker build -t ${image_name} .

lint:
	@autoflake --recursive --in-place --remove-unused-variables --remove-all-unused-imports --exclude app/api/shortcuts.py app
	@black .
	@isort .

echo:
	@echo ${image_name}