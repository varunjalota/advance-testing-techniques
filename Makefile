install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --v --cov=hello test_hello.py

lint:
	pylint --disable=R,C hello.py

all: install lint test
