build: clean
	pipenv install --dev
	pipenv update
	pipenv env python setup.py py2app

clean:
	rm -rf build dist
