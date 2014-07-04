deps:
	pip install -r requirements.txt

test: 
	py.test tests

pep8:
	@flake8 server --ignore=F403,F401
