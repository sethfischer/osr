"""Sphinx configuration."""

import os
from datetime import date

import sphinx_rtd_theme  # type: ignore[import-untyped] # noqa: F401


def canonical_url() -> str:
    """Canonical URL for built documentation."""
    if os.environ.get("READTHEDOCS_CANONICAL_URL"):
        return os.environ["READTHEDOCS_CANONICAL_URL"]

    return "http://localhost:8080"


project = "sethfischer-rover"
release = "0.1.0"
author = "Seth Fischer"
project_copyright = f"{date.today().year}, {author}"


exclude_patterns = ["_build"]
extensions = [
    "osr_sphinx",
    "sphinx.ext.graphviz",
    "sphinx_argparse_cli",
    "sphinx_design",
    "sphinx_rtd_theme",
    "sphinxcontrib.cadquery",
    "sphinxext.opengraph",
]
templates_path = [
    "_templates",
]


html_context = {
    "display_star_on_github": True,
}
html_favicon = "_static/images/icon.svg"
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_title = f"{project} v{release}"


linkcheck_allowed_redirects = {
    r"https://cadquery\.readthedocs\.io/.*": (
        r"https://cadquery\.readthedocs\.io/en/latest/.*"
    ),
    r"https://cq-electronics\.readthedocs\.io/.*": (
        r"https://cq-electronics\.readthedocs\.io/en/latest/.*"
    ),
    r"https://open-source-rover\.readthedocs\.io/.*": (
        r"https://open-source-rover\.readthedocs\.io/en/latest/.*"
    ),
    r"https://sphinxcontrib-cadquery\.readthedocs\.io/.*": (
        r"https://sphinxcontrib-cadquery\.readthedocs\.io/en/latest/.*"
    ),
    r"https://www\.sphinx-doc\.org/.*": r"https://www\.sphinx-doc\.org/en/master/.*",
}

linkcheck_ignore = [
    "https://roverchallenge.eu/",  # SSLCertVerificationError
    "https://www.kickstarter.com/",  # returns 403 for robots
]


cadquery_include_source = False


graphviz_output_format = "svg"


ogp_image = "_static/og-image-main.png"
ogp_site_url = canonical_url()
ogp_social_cards = {
    "enable": False,
}
