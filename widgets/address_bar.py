from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QLineEdit

from navigation_system import NavigationSystem


class AddressBar(QLineEdit):
    def __init__(self, navigation_system: NavigationSystem):
        super().__init__()
        self._navigation_system = navigation_system
        self.setText(navigation_system.current_url)
        self._navigation_system.url_changed.connect(self.on_url_changed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self._navigation_system.navigate_to(self.text())
        else:
            super().keyPressEvent(event)

    @Slot(str)
    def on_url_changed(self, url: str) -> None:
        self.setText(url)
