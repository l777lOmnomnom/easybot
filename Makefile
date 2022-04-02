SHELL = /bin/sh
PYTHON=python3.8

BUILD_DIR=build
PKG_DIR=dist
DOC_OUT_DIR=$(BUILD_DIR)/doc
PACKAGE_ROOT=$(PWD)

all: help

help:
	@echo "make documentation - Create API and manual."
	@echo ""
	@echo "make package       - Create a Python Built Distribution package."
	@echo ""
	@echo "make clean         - Clean generated files."

clean:
	find . -name '*.pyc' -delete
	$(RM) -rf $(BUILD_DIR)
	$(RM) -rf $(PKG_DIR)
	$(RM) -rf *.egg-info

install-python-dependencies:
	$(PYTHON) -m venv venv  && \
	. venv/bin/activate && \
	$(PYTHON) -m pip install -r requirements.txt
