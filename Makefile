compile_ext:
	python setup.py build_ext -i

setup:
	pip install -r test_requirements.txt

test: compile_ext
	env PYTHONPATH=$$PYTHONPATH:correios_frete/ pyvows --cover --cover-package=correios_frete -vvv

ci_test:
	$(MAKE) test
