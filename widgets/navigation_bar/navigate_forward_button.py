from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton

from services import BrowsingContext


class NavigateForwardButton(QPushButton):
    def __init__(self, browsing_context: BrowsingContext, parent=None):
        super().__init__(parent)

        self.__create_layout()

        # We listen for when the web view can go forward in the page history
        browsing_context.web_view_page_history_can_go_forward.connect(self.__on_web_view_page_history_can_go_forward)

        # We fire off a signal to go forward in the page history when the button is clicked
        self.clicked.connect(browsing_context.web_view_page_history_go_forward.emit)

    def __create_layout(self):
        self.setIcon(QIcon("./assets/icons/forward_arrow.svg"))
        self.setText("")
        self.setStyleSheet("QPushButton { border-radius: 5px; background-color: transparent; }")

    def __on_web_view_page_history_can_go_forward(self, can_go_forward: bool) -> None:
        # We enable or disable the button based on whether we can go forward in the page history
        self.setEnabled(can_go_forward)
