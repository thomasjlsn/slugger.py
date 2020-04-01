BIN ?= slugger
PREFIX ?= /usr/local

install:
	@cp $(BIN).py $(PREFIX)/bin/$(BIN)

uninstall:
	@rm $(PREFIX)/bin/$(BIN)

lint:
	@pylint3 slugger.py

test:
	@python3 test_slugger.py

commit: lint test
	@git commit


push: lint test
	@git push
