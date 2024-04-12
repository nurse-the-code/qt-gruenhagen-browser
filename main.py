import sys
from PySide6.QtWidgets import QApplication

from widgets import BrowserWindow

user_preferences = {
    "homepage": "https://github.com/nurse-the-code/qt-gruenhagen-browser"
}


class QtGruenhagenBrowser:
    def __init__(self):
        # Initialize the QApplication
        self._qt_app: QApplication = QApplication(sys.argv)
        self._browser_window: BrowserWindow = BrowserWindow(user_preferences)

    def run(self):
        # Execute the application and exit when the user closes the window
        sys.exit(self._qt_app.exec())


if __name__ == "__main__":
    browser = QtGruenhagenBrowser()
    browser.run()
