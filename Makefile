PYTHON ?= python3

.PHONY: all
all: index.html

index.html: problems.json Makefile tools/catalog.py tools/catalog.js tools/page.tpl \
            $(wildcard img/original/*.png img/corrected/*.png)
	@set -e; tmp=$$(mktemp '$@.XXXXXX'); trap 'rm -f "$$tmp"' EXIT; \
	  $(PYTHON) -B tools/catalog.py > "$$tmp"; chmod 644 "$$tmp"; mv "$$tmp" '$@'
