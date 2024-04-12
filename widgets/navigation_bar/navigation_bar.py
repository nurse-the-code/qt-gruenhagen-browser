from PySide6.QtWidgets import QToolBar

from .address_bar import AddressBar
from services import BrowsingContext


class NavigationBar(QToolBar):
    def __init__(self, browsing_context: BrowsingContext):
        super().__init__()
        self.setMovable(False)
        self.addWidget(AddressBar(browsing_context))
