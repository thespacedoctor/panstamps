# -*- coding: utf-8 -*-

from builtins import str
import sys
import os
from datetime import datetime, date, time
from mock import Mock as MagicMock
import re
from sphinx_markdown_parser.parser import MarkdownParser, CommonMarkParser
from sphinx_markdown_parser.transform import AutoStructify
import m2r
import codecs

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo',
              'sphinx.ext.mathjax', 'sphinx.ext.autosummary', 'sphinx.ext.coverage', 'sphinx.ext.linkcode', 'sphinxcontrib.mermaid', 'sphinx_search.extension']


class Mock(MagicMock):
    """AVOID INSTALLING THESE C-DEPENDENT PACKAGES"""
    @classmethod
    def __getattr__(cls, name):
        return Mock()
MOCK_MODULES = ['numpy', 'scipy', 'matplotlib', 'matplotlib.colors',
                'matplotlib.pyplot', 'matplotlib.cm', 'matplotlib.path', 'matplotlib.patches', 'matplotlib.projections', 'matplotlib.projections.geo', 'healpy', 'astropy', 'astropy.io', 'pylibmc', 'HMpTy', 'HMpTy.mysql', 'ligo', 'ligo.gracedb', 'ligo.gracedb.rest', 'pandas', 'astropy.stats']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# WHERE DOES THIS conf.py FILE LIVE?
moduleDirectory = os.path.dirname(os.path.realpath(__file__))
# GET PACKAGE __version__ INTO locals()
exec(open(moduleDirectory + "/../../panstamps/__version__.py").read())

sys.path.insert(0, os.path.abspath('../../panstamps/panstamps'))


autosummary_generate = True
autosummary_imported_members = True
autodoc_member_order = 'bysource'
add_module_names = False
todo_include_todos = True
templates_path = ['_static/whistles-theme/sphinx']
source_suffix = ['.rst', '.md']
master_doc = 'index'
# pygments_style = 'monokai'
html_theme = 'sphinx_rtd_theme'
html_logo = "_images/thespacedoctor_icon_white_circle.png"
html_favicon = "_images/favicon.ico"
html_show_sourcelink = True
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'github_user': 'thespacedoctor',
    'github_repo': 'panstamps',
    'strap_line': "Download stacked and/or warp image stamps from the STScI PanSTARRS image server via CL or Python API"
}
html_theme_path = ['_static/whistles-theme/sphinx/_themes']
# html_title = None
# html_short_title = None
# html_sidebars = {}
# html_last_updated_fmt = '%b %d, %Y'
# html_additional_pages = {}
html_show_copyright = True
html_show_sphinx = True
html_add_permalinks = u"  ∞"
html_static_path = ['_static']
html_file_suffix = None
trim_footnote_reference_space = True
# Add substitutions here
rst_epilog = u"""
.. |tsd| replace:: thespacedoctor
""" % locals()
link_resolver_url = "https://github.com/thespacedoctor/panstamps/tree/master"

# General information about the project.
now = datetime.now()
now = now.strftime("%Y")
project = u'panstamps'
copyright = u'%(now)s, Dave Young' % locals()
version = "v" + str(__version__)
release = version
today_fmt = '%Y'

exclude_patterns = ['_build', '_templates',
                    '**__version__.py', '**setup.py', 'api/panstamps.rst']
modindex_common_prefix = ["panstamps."]

# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'panstamps.tex', u'panstamps Documentation',
     u'Dave Young', 'manual'),
]
latex_logo = "_images/thespacedoctor_icon_dark.png"

markdown_parser_config = {
    'auto_toc_maxdepth': 4,
    'enable_auto_toc_tree': True,
    'enable_eval_rst': True,
    'enable_inline_math': True,
    'enable_math': True,
    'extensions': [
        'extra',
        'nl2br',
        'sane_lists',
        'smarty',
        'toc',
        'wikilinks',
        'pymdownx.arithmatex',
        'meta',
        'pymdownx.tilde',
        'pymdownx.critic',
        'pymdownx.tasklist',
        'mdx_include',
        'pymdownx.mark',
        'pymdownx.betterem',
        'pymdownx.caret',
        'legacy_attrs'
    ],
    'extension_configs': {
        'toc': {
            'marker': '1234TOC1234',
            'toc_depth': '2-5'
        },
        'pymdownx.tasklist': {
            'custom_checkbox': False,
            'clickable_checkbox': False
        },
        'mdx_include': {
            "base_path": moduleDirectory,
            "syntax_left": "\{\{",
            "syntax_right": "\}\}",
        }
    },
}


def updateUsageMd():
    """
    *Grab the usage from cl_utils.py to display in README.md*
    """
    from panstamps import cl_utils
    usage = cl_utils.__doc__

    if not "Usage:" in usage or "todo:" in usage:
        return None
    usageString = ""
    for l in usage.split("\n"):
        usageString += "    " + l + "\n"

    usage = """

```bash 
%(usageString)s
```
""" % locals()

    moduleDirectory = os.path.dirname(__file__)
    uFile = moduleDirectory + "/usage.md"
    writeFile = codecs.open(uFile, encoding='utf-8', mode='w')
    writeFile.write(usage)
    writeFile.close()

    return None


def generateAutosummaryIndex():

    import panstamps
    import inspect
    import os.path
    import time

    # CHECK FOR LAST MODIFIED TIME - DON'T UPDATE IF < 5 SEC
    # autobuild GOES INTO INFINITE LOOP OTHERWISE
    moduleDirectory = os.path.dirname(__file__)
    file = moduleDirectory + "/autosummary.rst"
    pathToWriteFile = file
    exists = os.path.exists(file)
    if not exists:
        pathToWriteFile = file
        try:
            writeFile = open(pathToWriteFile, 'w')
            writeFile.write("")
            writeFile.close()
        except IOError as e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            raise IOError(message)

    now = time.time()
    delta = now - os.path.getmtime(file)
    if delta < 5:
        return None

    # GET ALL SUBPACKAGES
    allSubpackages = ["panstamps"]
    allSubpackages += findAllSubpackges(
        pathToPackage="panstamps"
    )

    # INSPECT TO FIND ALL MODULES, CLASSES AND FUNCTIONS
    allModules = []
    allClasses = []
    allFunctions = []
    allMethods = []
    for sp in allSubpackages:
        for name, obj in inspect.getmembers(__import__(sp, fromlist=[''])):
            if inspect.ismodule(obj):
                if name in ["numpy"]:
                    continue
                thisMod = sp + "." + name
                if thisMod not in allSubpackages and len(name) and name[0:1] != "_" and name[-5:] != "tests" and name not in ["cl_utils", "inspect", "os"]:
                    allModules.append(sp + "." + name)
                # if thisMod not in allSubpackages and len(name) and name[0:2] != "__" and name[-5:] != "tests" and name != "cl_utils" and name != "utKit":
                #     allModules.append(sp + "." + name)

    moreModules = []
    for spm in allSubpackages + allModules:
        for name, obj in inspect.getmembers(__import__(spm, fromlist=[''])):
            if name[:2] == "__" or allSubpackages[0] not in name:
                continue
            try:
                moreModules.append(obj.__module__)
            except:
                pass

    for spm in allSubpackages + allModules + moreModules:
        for name, obj in inspect.getmembers(__import__(spm, globals(), locals(), fromlist=[''], level=0)):
            if name[:2] == "__":
                continue
            if spm.split(".")[-1] == name:
                continue
            if inspect.isclass(obj):
                thisClass = spm + "." + name
                if (thisClass == obj.__module__ or spm == obj.__module__) and len(name) and name[0:1] != "_":
                    allClasses.append(thisClass)
            if inspect.isfunction(obj):
                thisFunction = spm + "." + name
                if (spm == obj.__module__ or obj.__module__ == thisFunction) and len(name) and name != "main" and name[0:1] != "_":
                    allFunctions.append(thisFunction)
            if inspect.ismethod(obj):
                thisMethod = spm + "." + name
                if (spm == obj.__module__ or obj.__module__ == thisMethod) and len(name) and name != "main" and name[0:1] != "_":
                    allMethods.append(thisMethod)

    allSubpackages = allSubpackages[1:]
    allSubpackages.sort(reverse=False)
    allModules.sort()
    allClasses.sort()
    allFunctions.sort()
    allSubpackages = ("\n   ").join(allSubpackages)
    allModules = ("\n   ").join(allModules)
    allClasses = ("\n   ").join(allClasses)
    allFunctions = ("\n   ").join(allFunctions)

    # FOR SUBPACKAGES USE THE SUBPACKAGE TEMPLATE INSTEAD OF DEFAULT MODULE
    # TEMPLATE
    if len(allModules):
        thisText  = """
Modules
-------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:

   %(allSubpackages)s 
   %(allModules)s 

""" % locals()

    if len(allClasses):
        thisText += """
Classes
-------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:

   %(allClasses)s 

""" % locals()

    if len(allFunctions):
        thisText += """
Functions
---------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:

   %(allFunctions)s 
""" % locals()

    moduleDirectory = os.path.dirname(__file__)
    writeFile = codecs.open(
        moduleDirectory + "/autosummary.rst", encoding='utf-8', mode='w')
    writeFile.write(thisText)
    writeFile.close()

    regex = re.compile(r'\n\s*.*?utKit\.utKit(\n|$)', re.I)
    allClasses = regex.sub("\n", allClasses)

    autosummaryInclude = u"""
**Modules**

.. autosummary::
   :nosignatures:

   %(allSubpackages)s 
   %(allModules)s

**Classes**

.. autosummary::
   :nosignatures:

   %(allClasses)s 

**Functions**

.. autosummary::
   :nosignatures:

   %(allFunctions)s 
""" % locals()

    moduleDirectory = os.path.dirname(__file__)
    writeFile = codecs.open(
        moduleDirectory + "/autosummary_include.rst", encoding='utf-8', mode='w')
    writeFile.write(autosummaryInclude)
    writeFile.close()

    return thisText


def findAllSubpackges(
    pathToPackage
):
    import pkgutil
    importedPackage = __import__(
        pathToPackage, fromlist=[''])
    subPackages = []

    for importer, modname, ispkg in pkgutil.walk_packages(importedPackage.__path__, prefix=importedPackage.__name__ + '.',
                                                          onerror=lambda x: None):
        if ispkg and "tests" != modname[-5:] and "._" not in modname and ".tests." not in modname:
            subPackages.append(modname)

    return subPackages


def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    if info['fullname']:
        filename += "/" + info['fullname'] + ".py"
    return link_resolver_url + "/" + filename


def docstring(app, what, name, obj, options, lines):

    md = '\n'.join(lines)

    regex = re.compile(r'(.+?)\n:\s+(.*\n)')
    md = regex.sub(r'\1\n  \2', md)

    regex = re.compile(r'(\s|\n)(\$[^\$\n]+\$)([^\$])')
    md = regex.sub(r'\1`\2`\3', md)

    # FIX DEFINITIONS
    regex = re.compile(r'(( |\t)+)- ``([^\n]+)`` -')
    md = regex.sub(r"6473829123- `\3` -", md)

    # REMOVE STRIKETHROUGH
    regex = re.compile(r'~~([^~\n]+)~~ ?')
    md = regex.sub(r"", md)

    # ALLOW FOR CITATIONS TO SEMI-WORK (AS FOOTNOTES)
    regex = re.compile(r'\[#(.*?)\]')
    md = regex.sub(r"[^cn\1]", md)

    # SUBSCRIPT
    regex = re.compile(r'([!~]*\S)~(\S)([!~]*\n)')
    md = regex.sub(r"\1~\2~\3", md)
    regex = re.compile(r'([^\~])\~([^\~\n]+)\~([^\~])')
    index = 0
    while index < 100 and "~" in md:
        index += 1
        md = regex.sub(r'\1\\ :sub:`\2`\\\3', md, count=1)

    # SUPERSCRIPT
    regex = re.compile(r'([!\^]*\S)\^(\S)([!\^]*\n)')
    md = regex.sub(r"\1^\2^\3", md)
    regex = re.compile(r'([^\^])\^([^\^\n]+)\^([^\^])')
    index = 0
    while index < 100 and "^" in md:
        index += 1
        md = regex.sub(r'\1\\ :sup:`\2`\\\3', md, count=1)

    # HR
    regex = re.compile(r'\n---')
    md = regex.sub(r"\n\n----------\n\n", md)

    rst = md
    rst = m2r.convert(md)
    rst = rst.replace("6473829123", "  ")
    rst = rst.replace(".. code-block:: eval_rst", "")

    # REPLACE THE DOCSTRING LINES WITH OUR NEW RST
    lines.clear()
    for line in rst.split("\n"):
        lines.append(line)


def setup(app):
    app.connect('autodoc-process-docstring', docstring)
    app.add_source_suffix('.md', 'markdown')
    app.add_source_parser(MarkdownParser)
    app.add_config_value('markdown_parser_config',
                         markdown_parser_config, True)
    app.add_transform(AutoStructify)

# DO THE WORK
updateUsageMd()
autosummaryText = generateAutosummaryIndex()
