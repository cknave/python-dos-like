import importlib.metadata

# -- Project information -----------------------------------------------------

project = 'python-dos-like'
copyright = '2022, Kevin Vance'
author = 'kvance'

# The full version, including alpha/beta/rc tags
release = importlib.metadata.metadata('python-dos-like')['version']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_toolbox.more_autodoc.typehints',
]

# Hide "Return type: None" for sphinx_toolbox.more_autodoc.typehints
hide_none_rtype = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Links to external documentation
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),

    # see make-cffi-cdata.py:
    'cffi': ('https://cffi.readthedocs.io/en/latest/', 'cffi-cdata.inv'),
}

# Error if reference targets can't be found
nitpicky = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.']
html_css_files = ['styles.css']
