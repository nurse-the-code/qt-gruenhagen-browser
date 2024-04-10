from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow


class BrowserUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self._browser_view = QWebEngineView()
        self.setCentralWidget(self._browser_view)

        # Change the application name upon launch
        self.setWindowTitle("Qt Gruenhagen Browser")

    @property
    def browser_view(self):
        return self._browser_view

    def display(self):
        self.showFullScreen()