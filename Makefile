conda_env := static-site-generation
notebooks := $(wildcard notebook/*.ipynb) $(wildcard notebook/**/*.ipynb)
md_pages := $(patsubst notebook/%.ipynb,docs/%.md,$(notebooks))


all: init runtests

init:
	pip install -r requirements.txt

test:
	python3 -m unittest tests/*.py

# static site generation
build.env: ; conda env create -f environment.yml
build.site: $(md_pages) ; mkdir docs/img ; cp -r notebook/img/* docs/img ;

clean.env: ; conda remove --name $(conda_env) --all
clean.site: ; rm $(md_pages) ; rm -r docs/* ;

print-%: ; @echo $* is $($*):

docs/%.md: notebook/%.ipynb
	jupyter nbconvert\
		--to markdown $<\
		--output-dir $(dir $@)\
