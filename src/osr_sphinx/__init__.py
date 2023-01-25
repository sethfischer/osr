"""OSR Sphinx extension."""

from typing import Any

import sphinx.application

from osr_mechanical import __version__
from osr_sphinx.domain import OsrDomain


def setup(app: sphinx.application.Sphinx) -> dict[str, Any]:
    """Set up."""
    app.add_domain(OsrDomain)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
