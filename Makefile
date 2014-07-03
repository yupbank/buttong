deps:
	pip install -r requirements.txt

test: 
	cd server
	py.test server/tests

pep8:
	@flake8 server --ignore=F403,F401
