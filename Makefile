# Norsk Gjeldsinformasjon API Docs — Makefile
#
# Common operations for the MkDocs documentation site.
# Targets are self-contained — no manual venv activation needed.

SITE_DIR     = site
VENV         = env
REQS         = requirements.txt
MKDOCS_CFG   = mkdocs.yml
MKDOCS       = $(VENV)/bin/mkdocs

.DEFAULT_GOAL := build

# ── Help ──────────────────────────────────────────────────────────────────────

.PHONY: help build serve validate setup clean distclean
help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

# ── Setup ─────────────────────────────────────────────────────────────────────

.PHONY: setup
setup: $(VENV)/bin/mkdocs  ## Create virtualenv and install dependencies

$(VENV)/bin/mkdocs:
	test -d $(VENV) || python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r $(REQS)

# ── Build & Serve ─────────────────────────────────────────────────────────────

.PHONY: build
build: $(VENV)/bin/mkdocs  ## Build the static site (clean build)
	rm -rf $(SITE_DIR)
	$(MKDOCS) build --clean -f $(MKDOCS_CFG)

.PHONY: serve
serve: $(VENV)/bin/mkdocs  ## Start the dev server with live reload
	$(MKDOCS) serve -f $(MKDOCS_CFG)

# ── Validation ────────────────────────────────────────────────────────────────

.PHONY: validate
validate: $(VENV)/bin/mkdocs  ## Build in strict mode (clean build) to catch broken links and warnings
	$(MKDOCS) build --strict --clean -f $(MKDOCS_CFG)

# ── Clean ─────────────────────────────────────────────────────────────────────

.PHONY: clean
clean:  ## Remove build artefacts (site/)
	rm -rf $(SITE_DIR)

.PHONY: distclean
distclean: clean  ## Remove build artefacts and virtual environment (site/ + env/)
	rm -rf $(VENV)