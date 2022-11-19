"""Abstract base classes for CadQuery object containers."""

from abc import ABC, abstractmethod


class CqObjectContainer(ABC):
    """Abstract base class for CadQuery object containers."""

    @property
    @abstractmethod
    def cq_object(self):
        """Get CadQuery object."""
        pass

    @abstractmethod
    def _make(self):
        """Create CadQuery object."""
        pass
