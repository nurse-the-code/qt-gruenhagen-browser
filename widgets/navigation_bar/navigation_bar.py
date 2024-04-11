from PySide6.QtWidgets import QToolBar

from navigation_system import NavigationSystem
from .address_bar import AddressBar


class NavigationBar(QToolBar):
    def __init__(self, navigation_system: NavigationSystem):
        super().__init__()
        self._navigation_system: NavigationSystem = navigation_system
        self.setMovable(False)
        self.addWidget(AddressBar(self._navigation_system))