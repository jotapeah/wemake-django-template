# wemake-django-template documentation build configuration file, created by
# sphinx-quickstart on Sat Sep 30 12:42:34 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from pathlib import Path
from typing import cast

import django
import tomli

# We need `server` to be importable from here:
_ROOT = Path('..').resolve(strict=True)
sys.path.insert(0, str(_ROOT))

# Django setup, all deps must be present to succeed:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()


# -- Project information -----------------------------------------------------


def _get_project_meta() -> dict[str, str]:  # lying about return type
    pyproject = _ROOT / 'pyproject.toml'
    return cast(
        dict[str, str],
        tomli.loads(pyproject.read_text())['project'],
    )


pkg_meta = _get_project_meta()
project = pkg_meta['name']

# The short X.Y version
version = pkg_meta['version']
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    # https://github.com/executablebooks/MyST-Parser
    'myst_parser',
    # 3rd party, order matters:
    # https://github.com/wemake-services/wemake-django-template/issues/159
    'sphinx_autodoc_typehints',
]

# If true, Sphinx will warn about all references
# where the target cannot be found. Default is `False``.
# You can activate this mode temporarily using the `-n` command-line switch.
nitpicky = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
