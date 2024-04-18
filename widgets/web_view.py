from PySide6.QtCore import QUrl, Slot
from PySide6.QtWebEngineWidgets import QWebEngineView

from services import BrowsingContext


class WebView(QWebEngineView):
    def __init__(self, browsing_context: BrowsingContext, parent=None):
        super().__init__(parent)
        # First we unpack signals from the browsing context
        self.__new_url_address_entered = browsing_context.new_url_address_entered
        self.__web_view_url_changed = browsing_context.web_view_url_changed
        self.__web_view_page_history_can_go_back = browsing_context.web_view_page_history_can_go_back
        self.__web_view_page_history_can_go_forward = browsing_context.web_view_page_history_can_go_forward
        self.__web_view_page_history_go_back = browsing_context.web_view_page_history_go_back
        self.__web_view_page_history_go_forward = browsing_context.web_view_page_history_go_forward

        self.__connect_signals()

        # Finally, we navigate to the homepage
        self.__navigate_to(browsing_context.homepage)

    def __connect_signals(self):
        # We listen for when the user enters a new URL in the address bar
        self.__new_url_address_entered.connect(self.__on_address_bar_new_url_entered)

        # When the web view's URL changes, we emit the signal
        self.urlChanged.connect(self.__on_web_view_url_changed)

        # We listen for requests to go back and forward in the page history
        self.__web_view_page_history_go_back.connect(self.__on_go_back_request)
        self.__web_view_page_history_go_forward.connect(self.__on_go_forward_request)

    def __navigate_to(self, url: QUrl) -> None:
        self.load(url)

    @Slot(QUrl)
    def __on_address_bar_new_url_entered(self, url: QUrl) -> None:
        self.__navigate_to(url)

    @Slot(QUrl)
    def __on_web_view_url_changed(self, url: QUrl) -> None:
        self.__web_view_url_changed.emit(url)
        self.__web_view_page_history_can_go_back.emit(self.history().canGoBack())
        self.__web_view_page_history_can_go_forward.emit(self.history().canGoForward())

    @Slot()
    def __on_go_back_request(self) -> None:
        if self.page().history().canGoBack():
            self.page().history().back()

    @Slot()
    def __on_go_forward_request(self) -> None:
        if self.page().history().canGoForward():
            self.page().history().forward()
