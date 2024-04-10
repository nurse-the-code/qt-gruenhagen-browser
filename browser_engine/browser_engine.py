from PySide6.QtCore import QUrl

from browser_ui import BrowserUI
from core import NavigationSystem


class BrowserEngine:
    def __init__(self, browser_ui: BrowserUI, navigation_system: NavigationSystem):
        self._browser_ui = browser_ui
        self._navigation_system = navigation_system
        self.navigate_to(self._navigation_system.home_url)

    def navigate_to(self, url):
        def on_navigation(callback_url):
            self._browser_ui.browser_view.setUrl(QUrl(callback_url))
        self._navigation_system.navigate_to(url, on_navigation)
