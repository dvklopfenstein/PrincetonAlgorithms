
pylint:
	@git status -uno | perl -ne 'if (/(\S+.py)/) {printf "echo $$1\npylint -r no %s\n", $$1}' | tee tmp_pylint
	chmod 755 tmp_pylint
	tmp_pylint

clean:
	rm -f tmp_pylint

.PHONY: py
py:
	find . -name \*.py
