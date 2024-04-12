from PySide6.QtCore import QUrl, Signal
from PySide6.QtWidgets import QMainWindow

from services import BrowsingContext
from .web_view import WebView
from .navigation_bar import NavigationBar


class BrowserWindow(QMainWindow):
    new_url_address_entered = Signal(QUrl)
    web_view_url_changed = Signal(QUrl)

    def __init__(self, user_preferences: dict):
        super().__init__()
        self.homepage = user_preferences["homepage"]
        self.browsing_context: BrowsingContext = self.create_navigation_context()
        self._web_view: WebView = WebView(self.browsing_context)
        self._navigation_bar: NavigationBar = NavigationBar(self.browsing_context)
        self.create_layout()
        self.showFullScreen()

    def create_layout(self):
        self.setWindowTitle("Qt Gruenhagen Browser")
        self.addToolBar(self._navigation_bar)
        self.setCentralWidget(self._web_view)

    def create_navigation_context(self) -> BrowsingContext:
        return BrowsingContext(
            homepage=QUrl(self.homepage),
            new_url_address_entered=self.new_url_address_entered,
            web_view_url_changed=self.web_view_url_changed
        )
