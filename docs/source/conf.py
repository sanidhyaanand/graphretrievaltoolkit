# Configuration file for the Sphinx documentation builder.

import os.path as osp
import sys

sys.path.insert(0, osp.abspath('../../'))

# -- Project information

project = 'GRT'
# copyright = ''
author = 'Sanidhya Anand'

# release = ''
# version = ''

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
autodoc_member_order = 'bysource'

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'