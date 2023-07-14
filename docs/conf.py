# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import sys
import datetime

sys.path.insert(0, os.path.abspath(".."))

try:
    # Inject mock modules so that we can build the
    # documentation without having the real stuff available
    from mock import Mock

    to_be_mocked = [
        "micropython",
        "machine",
    ]
    for module in to_be_mocked:
        sys.modules[module] = Mock()
        print("Mocked '{}' module".format(module))

    import micropython_mlx90393
except ImportError:
    raise SystemExit("micropython_mlx90393 has to be importable")

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_immaterial",
]

autodoc_preserve_defaults = True


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "MicroPython": ("https://docs.micropython.org/en/latest/", None),
}

autoclass_content = "both"
templates_path = ["_templates"]
source_suffix = ".rst"
# The master toctree document.
master_doc = "index"

# General information about the project.
project = "MicroPython_MLX90393 Library"
creation_year = "2023"
current_year = str(datetime.datetime.now().year)
year_duration = (
    current_year
    if current_year == creation_year
    else creation_year + " - " + current_year
)
copyright = year_duration + " Jose D. Montoya"
author = "Jose D. Montoya"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"
html_baseurl = "https://micropython-mlx90393.readthedocs.io/"
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".env", "requirements.txt"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
#
add_function_parentheses = True

rst_prolog = """
.. role:: python(code)
   :language: python
   :class: highlight
.. default-literal-role:: python
"""

todo_include_todos = False
todo_emit_warnings = False
napoleon_numpy_docstring = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_immaterial"

html_theme_options = {
    "features": [
        "search.share",
    ],
    # Set the color and the accent color
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "purple",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/jposada202020/MicroPython_MLX90393/",
    "repo_name": "MicroPython MLX90393",
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/jposada202020/MicroPython_MLX90393",
        },
        {
            "icon": "fontawesome/brands/python",
            "link": "https://pypi.org/project/micropython-mlx90393/",
        },
        {
            "name": "MicroPython Downloads",
            "icon": "octicons/download-24",
            "link": "https://micropython.org",
        },
    ],
}

sphinx_immaterial_custom_admonitions = [
    {
        "name": "warning",
        "color": (255, 66, 66),
        "icon": "octicons/alert-24",
        "override": True,
    },
    {
        "name": "note",
        "icon": "octicons/pencil-24",
        "override": True,
    },
    {
        "name": "seealso",
        "color": (255, 66, 252),
        "icon": "octicons/eye-24",
        "title": "See Also",
        "override": True,
    },
    {
        "name": "hint",
        "icon": "material/school",
        "override": True,
    },
    {
        "name": "tip",
        "icon": "material/school",
        "override": True,
    },
    {
        "name": "important",
        "icon": "material/school",
        "override": True,
    },
]

python_type_aliases = {
    "DigitalInOut": "digitalio.DigitalInOut",
}

object_description_options = [
    ("py:.*", dict(generate_synopses="first_sentence")),
]

# Set link name generated in the top bar.
html_title = "MicroPython MLX90393"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["extra_css.css"]

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "_static/favicon.ico"

html_logo = "_static/Logo.png"
# Output file base name for HTML help builder.
htmlhelp_basename = "MicropythonMLX90393Librarydoc"
