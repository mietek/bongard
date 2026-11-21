PANDOC ?= pandoc
PYTHON ?= python3

pages := index.html problems.html flagged.html

.PHONY: all
all: $(pages)

problems.html: tools/zoom.py $(wildcard img/derived/*D.svg)
problems.html: zoom := --variable=zoom

define render
	@set -e; tmp='$@.tmp'; trap 'rm -f "$$tmp"' EXIT; \
	  title=$$(sed -n '1s/^# //p' '$<'); \
	  $(PANDOC) --from=markdown-smart --to=html5 --wrap=none \
	    --template=tools/page.tpl --metadata="title:$$title" $(zoom) \
	    '$<' -o "$$tmp"; \
	  if [ '$@' = problems.html ]; then $(PYTHON) tools/zoom.py "$$tmp"; fi; \
	  mv "$$tmp" '$@'
endef

index.html: README.md Makefile tools/page.tpl
	$(render)

problems.html flagged.html: %.html: %.md Makefile tools/page.tpl
	$(render)
