# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import re
import os
import sys
import datetime as dt


project = 'Technical Reference Manual'
copyright = ', INTERMAGNET'
author = 'Technical Manual Team'
release = re.sub('^v', '', os.popen('git describe').read().strip())
release ='0.0.1'
version = release


file_dir = os.path.dirname(os.path.realpath(__file__))
year = dt.datetime.now().year
copyright = str(year) + copyright
variables_to_export = [
    "project",
    "copyright",
    "version",
]
frozen_locals = dict(locals())
rst_epilog = '\n'.join(map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export))
del frozen_locals

# -- General configuration ---------------------------------------------------
# Activate autosectionlabel plugin
# default_role = 'obj'
autosectionlabel_prefix_document = False
numfig = True
#navtree_shift = True
#navtree_root_links = True


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = ['sphinx_rtd_theme',
             ]




# Add any paths that contain templates here, relative to this directory.
# some comment
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build','docs', 'Thumbs.db', '.DS_Store','venv','appendices/includes']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_css_files = ['theme_overrides.css',]


latex_engine = 'xelatex'
latex_use_xindy = False


#added to avoid empty pages
latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',

}



latex_documents = [
    ('index', 'technical_manual_'+release+'.tex',
     u'INTERMAGNET Technical Reference Manual',
     u'', 'manual'),
]


