from PySide6.QtCore import Slot

from services import BrowsingContext

from .navigation_button import NavigationButton


class NavigateForwardButton(NavigationButton):
    def __init__(self, browsing_context: BrowsingContext, parent=None):
        super().__init__("./assets/icons/forward_arrow.svg", parent)

        # We listen for when the web view can go forward in the page history
        browsing_context.web_view_page_history_can_go_forward.connect(self.__on_web_view_page_history_can_go_forward)

        # We fire off a signal to go forward in the page history when the button is clicked
        self.clicked.connect(browsing_context.web_view_page_history_go_forward.emit)

    @Slot(bool)
    def __on_web_view_page_history_can_go_forward(self, can_go_forward: bool) -> None:
        # We enable or disable the button based on whether we can go forward in the page history
        self.setEnabled(can_go_forward)
