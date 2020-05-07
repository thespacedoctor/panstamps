# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build
SOURCEDIR     = source
ASDIR         = source/_autosummary
APIDIR        = source/_api
INDIR         = source/_includes

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source 
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	
	rm -rf $(BUILDDIR)/html/todo.html
	rm -rf $(ASDIR)
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -q -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -q -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

buildapi:
	# f force
	# P private modules
	# T no toc
	# e separate module pages
	# M module before submodules docs
	# F full project with quickstart
	# members  automatically document members
	# undoc-members include members without docstrings
	# private-members include _members
	# inherited-members  members inherited from baseclass
	# show-inheritance  show where code is inherited from
	rm -rf $(APIDIR)
	SPHINX_APIDOC_OPTIONS='members,undoc-members,show-inheritance,inherited-members,member-order' sphinx-apidoc -fMeTP  -o source/_api ../ ../setup.py ../panstamps/__version__.py ../*/tests* ../*/*/tests* ../*/*/*/tests* ../*/*/*/*/tests*
	@echo "Auto-generation of API documentation finished. " \
		"The generated files are in '_api/'"

