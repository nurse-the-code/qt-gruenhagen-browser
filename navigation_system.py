from PySide6.QtCore import QObject, QUrl, Signal


class NavigationSystem(QObject):
    url_changed = Signal(str)

    def __init__(self, home_url: str):
        super().__init__()
        self._home_url: str = self._urlify(home_url)
        self._current_url: str = self._urlify(home_url)

    @property
    def home_url(self) -> str:
        return self._home_url

    @property
    def current_url(self) -> str:
        return self._current_url

    def navigate_to(self, url: str) -> None:
        self._current_url: str = self._urlify(url)
        self.url_changed.emit(self._current_url)

    def navigate_home(self) -> None:
        self.navigate_to(self.home_url)

    @staticmethod
    def _urlify(url: str) -> str:
        return QUrl(url).toString()
