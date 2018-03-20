build: clean
	python setup.py py2app

clean:
	rm -rf build dist
