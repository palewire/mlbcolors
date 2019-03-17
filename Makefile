.PHONY: test ship

test:
	flake8 mlbcolors
	python test.py

ship:
	rm -rf build/
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing
