
all: init runtests

init:
	pip install -r requirements.txt

test:
	python3 -m unittest tests/*.py

