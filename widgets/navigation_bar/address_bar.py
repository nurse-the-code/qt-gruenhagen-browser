from PySide6.QtCore import Qt, QUrl, Slot
from PySide6.QtWidgets import QLineEdit

from services import BrowsingContext


class AddressBar(QLineEdit):
    def __init__(self, browsing_context: BrowsingContext):
        super().__init__()
        self.setPlaceholderText("Enter URL")
        self.__new_url_address_entered = browsing_context.new_url_address_entered
        browsing_context.web_view_url_changed.connect(self.on_web_view_url_changed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.__new_url_address_entered.emit(self.text())
        else:
            super().keyPressEvent(event)

    @Slot(QUrl)
    def on_web_view_url_changed(self, url: QUrl) -> None:
        self.setText(url.toString())
