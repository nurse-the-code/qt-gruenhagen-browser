import sys
from PySide6.QtWidgets import QApplication

from core import NavigationSystem
from browser_ui import BrowserUI
from browser_engine import BrowserEngine


class QtGruenhagenBrowser:
    def __init__(self):
        # My core application logic
        self._navigation = NavigationSystem()

        # Interfacing with the Qt framework
        self._qt_app = QApplication(sys.argv)
        self._browser_ui = BrowserUI()
        self._browser_engine = BrowserEngine(self._browser_ui, self._navigation)

    def run(self):
        self._browser_ui.display()
        sys.exit(self._qt_app.exec())


if __name__ == "__main__":
    browser = QtGruenhagenBrowser()
    browser.run()
