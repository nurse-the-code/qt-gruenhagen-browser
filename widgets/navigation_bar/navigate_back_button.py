from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton

from services import BrowsingContext


class NavigateBackButton(QPushButton):
    def __init__(self, browsing_context: BrowsingContext, parent=None):
        super().__init__(parent)

        self.create_layout()

        # We listen for when the web view can go back in the page history
        browsing_context.web_view_page_history_can_go_back.connect(self.on_web_view_page_history_can_go_back)

        # We fire off a signal to go back in the page history when the button is clicked
        self.clicked.connect(browsing_context.web_view_page_history_go_back.emit)

    def create_layout(self):
        self.setIcon(QIcon("./assets/icons/back_arrow.svg"))
        self.setText("")
        self.setStyleSheet("QPushButton { border-radius: 5px; background-color: transparent; }")

    def on_web_view_page_history_can_go_back(self, can_go_back: bool) -> None:
        # We enable or disable the button based on whether we can go back in the page history
        self.setEnabled(can_go_back)
