
all: init runtests

init:
	pip install -r requirements.txt

runtests:
	python3 -m unittest test.module

