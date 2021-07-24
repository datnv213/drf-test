run:
	python manage.py runserver

format:
	@echo "--------- black ---------"
	@black .
	@echo "--------- isort ---------"
	@isort .
	@echo "--------- black ---------"
	@black .
