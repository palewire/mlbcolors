.PHONY: test ship npmprep

npmprep:
	rm -rf `pwd`/build
	mkdir `pwd`/build
	cp mlbcolors/data.json build/mlbcolors.json

test:
	flake8 mlbcolors
	python test.py

ship:
	rm -rf build/
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing
