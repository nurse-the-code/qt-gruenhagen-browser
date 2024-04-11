from PySide6.QtWidgets import QMainWindow

from navigation_system import NavigationSystem
from widgets.web_view import WebView
from widgets.navigation_bar import NavigationBar


class BrowserWindow(QMainWindow):
    def __init__(self, navigation_system: NavigationSystem):
        super().__init__()
        self._navigation_system = navigation_system
        self._web_view = WebView(navigation_system)
        self._navigation_bar = NavigationBar(navigation_system)
        self.create_layout()
        self.showFullScreen()

    def create_layout(self):
        self.addToolBar(self._navigation_bar)
        self.setCentralWidget(self._web_view)
