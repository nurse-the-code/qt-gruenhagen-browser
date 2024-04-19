from PySide6.QtWebEngineWidgets import QWebEngineView

from engine import BrowsingContext, WebPage


class WebView(QWebEngineView):
    def __init__(self, browsing_context: BrowsingContext, parent=None):
        super().__init__(parent)
        self.setPage(WebPage(browsing_context, parent))
