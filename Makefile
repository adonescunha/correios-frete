compile_ext:
	python setup.py build_ext -i

setup:
	pip install -r test_requirements.txt

test: compile_ext
	env PYTHONPATH=. coverage run --source=correios_frete ./vows/__main__.py

ci_test:
	$(MAKE) test
