from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton


class NavigationButton(QPushButton):
    def __init__(self, icon_path: str, parent=None):
        super().__init__(parent)

        self.__create_layout(icon_path)

    def __create_layout(self, icon_path: str):
        self.setIcon(QIcon(icon_path))
        self.setText("")
        self.setIconSize(QSize(24, 24))
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                width: 24px;
                height: 24px;
            }
        """)
