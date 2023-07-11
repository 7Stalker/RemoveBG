install:
	pip install Pipfile && \
	Pipfile install

start:
	Pipfile run python app.py
