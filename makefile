.PHONY: py
py:
	fine tests py -name \*.py

p:
	find py -name \*.py

t:
	find tests -name \*.py

pylint:
	@git status -uno | perl -ne 'if (/(\S+.py)/) {printf "echo $$1\npylint -r no %s\n", $$1}' | tee tmp_pylint
	chmod 755 tmp_pylint
	tmp_pylint

clean:
	rm -f tmp_pylint
