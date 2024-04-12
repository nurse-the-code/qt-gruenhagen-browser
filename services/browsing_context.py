from PySide6.QtCore import QUrl, Signal


class BrowsingContext:
    def __init__(self, homepage: QUrl, new_url_address_entered: Signal, web_view_url_changed: Signal):
        self.homepage = homepage
        self.new_url_address_entered = new_url_address_entered
        self.web_view_url_changed = web_view_url_changed
