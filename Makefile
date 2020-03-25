BIN ?= slugger
PREFIX ?= /usr/local

install:
	@cp $(BIN).py $(PREFIX)/bin/$(BIN)

uninstall:
	@rm $(PREFIX)/bin/$(BIN)
