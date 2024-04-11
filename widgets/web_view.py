from PySide6.QtCore import QUrl, Slot
from PySide6.QtWebEngineWidgets import QWebEngineView

from navigation_system import NavigationSystem


class WebView(QWebEngineView):
    def __init__(self, navigation_system: NavigationSystem):
        super().__init__()
        self._navigation_system: NavigationSystem = navigation_system
        self.setUrl(QUrl(navigation_system.home_url))
        self._navigation_system.url_changed.connect(self.on_navigation_url_changed)
        self.urlChanged.connect(self.on_web_view_url_changed)

    @Slot(str)
    def on_navigation_url_changed(self, url: str) -> None:
        self.setUrl(QUrl(url))

    @Slot(QUrl)
    def on_web_view_url_changed(self, url: QUrl) -> None:
        self._navigation_system.navigate_to(url.toString())
