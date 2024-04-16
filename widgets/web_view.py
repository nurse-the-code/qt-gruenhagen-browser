from PySide6.QtCore import QUrl, Slot
from PySide6.QtWebEngineWidgets import QWebEngineView

from services import BrowsingContext


class WebView(QWebEngineView):
    def __init__(self, browsing_context: BrowsingContext):
        super().__init__()
        # First, we navigate to the homepage
        self.navigate_to(browsing_context.homepage)

        # We listen for when the user enters a new URL in the address bar
        browsing_context.new_url_address_entered.connect(self.on_address_bar_new_url_entered)
        # We get the signal for when the web view's URL changes
        self.__web_view_url_changed = browsing_context.web_view_url_changed

        # When the web view's URL changes, we emit the signal
        self.urlChanged.connect(self.on_web_view_url_changed)

    def navigate_to(self, url: QUrl) -> None:
        self.load(url)

    @Slot(QUrl)
    def on_address_bar_new_url_entered(self, url: QUrl) -> None:
        self.navigate_to(url)

    @Slot(QUrl)
    def on_web_view_url_changed(self, url: QUrl) -> None:
        self.__web_view_url_changed.emit(url.toString())
