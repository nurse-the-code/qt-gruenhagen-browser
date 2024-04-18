from PySide6.QtCore import QObject, QUrl, Signal


class BrowsingContext(QObject):
    new_url_address_entered: Signal = Signal(QUrl)
    web_view_url_changed: Signal = Signal(QUrl)
    web_view_page_history_can_go_back: Signal = Signal(bool)
    web_view_page_history_can_go_forward: Signal = Signal(bool)
    web_view_page_history_go_back: Signal = Signal()
    web_view_page_history_go_forward: Signal = Signal()

    def __init__(self, homepage: QUrl):
        super().__init__()
        self.homepage = homepage
