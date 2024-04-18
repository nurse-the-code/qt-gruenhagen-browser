from PySide6.QtCore import Qt, QUrl, Signal, Slot
from PySide6.QtWidgets import QLineEdit

from services import BrowsingContext


class AddressBar(QLineEdit):
    def __init__(self, browsing_context: BrowsingContext, parent=None):
        super().__init__(parent)
        # In case there is no URL, we set a placeholder text
        self.setPlaceholderText("Enter URL")

        self.setStyleSheet("""
            QLineEdit {
                height: 32px;
                padding-left: 16px;
                padding-right: 16px;
                border-radius: 16px;
            }
        """)

        # We get the signal for when the user enters a new URL in the address bar
        self.__new_url_address_entered: Signal = browsing_context.new_url_address_entered

        # We listen for when the web view's URL changes
        browsing_context.web_view_url_changed.connect(self.__on_web_view_url_changed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            # When the user presses the Enter key, we emit a signal with the new URL
            self.__new_url_address_entered.emit(self.text())
        else:
            # Since we're not handling the event, we call the parent class's method
            super().keyPressEvent(event)

    @Slot(QUrl)
    def __on_web_view_url_changed(self, url: QUrl) -> None:
        # When the web view's URL changes, we update the address bar's text
        self.setText(url.toString())
