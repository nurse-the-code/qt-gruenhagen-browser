class NavigationSystem:
    def __init__(self):
        self._home_url = "https://github.com/nurse-the-code/qt-gruenhagen-browser"
        self._current_url = self._home_url

    @property
    def home_url(self):
        return self._home_url

    @property
    def current_url(self):
        return self._current_url

    def navigate_to(self, url, navigation_callback):
        self._current_url = url
        navigation_callback(self._current_url)
