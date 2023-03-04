# advance-testing-techniques
This is a repo for doing Advance Testing 

# Running Test Cases with actions
[![Python application test with Github Actions](https://github.com/varunjalota/advance-testing-techniques/actions/workflows/main.yml/badge.svg)](https://github.com/varunjalota/advance-testing-techniques/actions/workflows/main.yml)

# Setup
1. Create and source Virtual Env
```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```

2. Scaffold
```bash
touch Makefile && touch test_hello.py && touch hello.py && requirements.txt
```

3. Create Makefile
```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```
### How to debug
* Print
* pdb
* testing
