"""Was an attempt at Abstract Class. But what I wanted to do actually doesn't work. TO REMOVE"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controllers.app_controller import AppController


class SubController(ABC):
    """Allow subcontrollers to reference the App Controller via a controller protected variable"""
    @property
    def controller(self) -> 'AppController':
        return self._controller

    @controller.setter
    def controller(self, controller: 'AppController') -> None:
        self._controller = controller

    @abstractmethod
    def run(self):
        """SubControllers must have a run method."""
        pass

