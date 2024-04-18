from PySide6.QtCore import QUrl, Signal
from PySide6.QtWidgets import QMainWindow

from services import BrowsingContext

from .navigation_bar import NavigationBar
from .web_view import WebView


class BrowserWindow(QMainWindow):
    new_url_address_entered = Signal(QUrl)
    web_view_url_changed = Signal(QUrl)

    def __init__(self, user_preferences: dict):
        super().__init__()
        # Create the browsing context
        self.__homepage = user_preferences["homepage"]
        self.__browsing_context: BrowsingContext = BrowsingContext(self.__homepage)

        # Create widgets
        self.__web_view: WebView = WebView(self.__browsing_context)
        self.__navigation_bar: NavigationBar = NavigationBar(self.__browsing_context)

        self.create_layout()

        # I've had issues with the window not showing up properly in the past when this was not last
        self.showFullScreen()

    def create_layout(self):
        self.setWindowTitle("Qt Gruenhagen Browser")
        self.addToolBar(self.__navigation_bar)
        self.setCentralWidget(self.__web_view)
