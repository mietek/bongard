PANDOC ?= pandoc
PYTHON ?= python3

.PHONY: all
all: index.html problems.html

index.html: README.md Makefile tools/page.tpl tools/omit-alt.lua
	$(PANDOC) --from=markdown-smart --to=html5 --wrap=none \
	  --template=tools/page.tpl --lua-filter=tools/omit-alt.lua \
	  --metadata="title:$$(sed -n '1s/^# //p' '$<')" '$<' -o '$@'

problems.html: problems.json Makefile tools/catalog.py tools/catalog.js tools/page.tpl \
               tools/zoom.py $(wildcard img/derived/*D.svg img/derived/individual/*.svg)
	@set -e; tmp=$$(mktemp '$@.XXXXXX'); trap 'rm -f "$$tmp"' EXIT; \
	  $(PYTHON) -B tools/catalog.py > "$$tmp"; chmod 644 "$$tmp"; mv "$$tmp" '$@'
