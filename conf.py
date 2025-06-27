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
import os
import re
import datetime as dt


project = 'Technical Reference Manual'
copyright = ', INTERMAGNET'
author = 'Technical Manual Team'
github_user = 'INTERMAGNET'
github_repo = 'imag-tech-man'
git_version_type = os.environ.get("READTHEDOCS_VERSION_TYPE") or 'local-dev'# tag, external, branch, unknown
git_branch_name = os.environ.get("READTHEDOCS_VERSION_NAME")
git_id = os.environ.get("READTHEDOCS_GIT_IDENTIFIER")
git_commit_hash = os.environ.get("READTHEDOCS_GIT_COMMIT_HASH")

if git_version_type == 'local-dev':
    git_branch_name = re.sub('^v', '', os.popen('git branch --show-current').read().strip())
    if(git_branch_name ==''):
        git_id = re.sub('^v', '', os.popen('git describe').read().strip())
    else:
        git_id = re.sub('^v', '', os.popen('git rev-parse --short HEAD').read().strip())
    git_commit_hash = git_id


print("---------------------------")
print(git_version_type)
print(git_branch_name)
print(git_id)
print(git_commit_hash)
#print(re.sub('^v', '', os.popen('git describe').read().strip()))
#print(re.sub('^v', '', os.popen('git describe --tags '+git_commit_hash).read().strip()))
#print(re.sub('^v', '', os.popen('git describe --tags HEAD').read().strip()))
print("---------------------------")



def is_dev_stream() -> bool:
    return (git_version_type == 'branch') and git_branch_name != 'latest'

def is_release() -> bool:
    return git_version_type == 'tag'

def get_html_context():
    if is_dev_stream():
        return {
            'display_github': True,
            'github_user': github_user,
            'github_repo': github_repo,
            'github_version': git_branch_name+'/'
        }
    else:
        return {}
def get_version_tag():
    if is_release():
        #current work around waiting for bugfix #11662 readthedocs.org
        return re.sub('^v', '', os.popen('git describe --tags '+git_commit_hash).read().strip())
        #return git_id
    else:
        return git_commit_hash[:7]

release = get_version_tag()
version = release


#release = re.sub('^v', '', os.popen('git describe').read().strip())
#release ='5.1.0-draft'



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
              "sphinx.ext.viewcode"
              #'sphinx.ext.imgmath',
              #'sphinx.ext.autosectionlabel',
              #'sphinx.ext.autodoc'
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

html_context = get_html_context()


latex_engine = 'xelatex'
latex_use_xindy = False


latex_appendices = ['appendices/terminology',
                    'appendices/observatories',
                    'appendices/archivedataformats',
                    'appendices/imagaddresses',
                    'appendices/dataformats',
                    'appendices/filters',
                    'appendices/acknowledgements'
                    ]

preamble = r'''
    \makeatletter
      \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
        \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\leftmark}}}
        \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
        \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
      }
    \usepackage{multicol}  
    \usepackage[none]{hyphenat}
    \setlength\parindent{12pt}
    \usepackage{enumitem}
    \setlist{noitemsep}
    \setlength{\parindent}{0cm}
    '''
file_dir = file_dir.replace("\\", "/")
latex_maketitle =  r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1
        \begin{titlepage}
            \begin{figure}
                \includegraphics[width = 1\textwidth,scale=1.2]{''' +file_dir + r'''/img/cover_intermagnet.png}
            \end{figure}
            \centering
            \vspace{10mm}
            \Huge \textbf{{INTERMAGNET}} \\
            \vspace{5mm}
            \Large \textbf{{Technical Reference Manual}} \\
            \vspace{70mm}
            \Large version : \ ''' + str(release) + ''' \ (''' + str(year) +r''') 
            \vspace*{0mm}
            \break     
            \break     
            \break     
            \break     
            \break     
            \break     
        \end{titlepage}
        \clearpage
        \pagenumbering{roman}
        '''
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
    'printindex': '',
    'preamble': preamble,
    'maketitle':latex_maketitle
}



latex_documents = [
    ('index', 'technical_manual_'+release+'.tex',
     u'INTERMAGNET Technical Reference Manual',
     u'', 'manual'),
]


