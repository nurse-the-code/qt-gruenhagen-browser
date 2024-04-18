from PySide6.QtWidgets import QToolBar

from services import BrowsingContext

from .address_bar import AddressBar
from .navigate_back_button import NavigateBackButton
from .navigate_forward_button import NavigateForwardButton


class NavigationBar(QToolBar):
    def __init__(self, browsing_context: BrowsingContext):
        super().__init__()
        self.setMovable(False)
        self.addWidget(NavigateBackButton(browsing_context))
        self.addWidget(NavigateForwardButton(browsing_context))
        self.addWidget(AddressBar(browsing_context))
