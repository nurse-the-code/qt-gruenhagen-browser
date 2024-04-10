import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView


class PicoBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()  # Create a QWebEngineView object
        self.browser.setUrl(QUrl("https://github.com/nurse-the-code/qt-gruenhagen-browser"))  # Load a web page
        self.setCentralWidget(self.browser)  # Set the browser as the central widget
        self.showMaximized()  # Maximize the window


if __name__ == "__main__":
    # Initialize the QApplication
    app = QApplication(sys.argv)
    # Create an instance of the PicoBrowser
    pico_browser = PicoBrowser()
    # Execute the application and exit when the user closes the window
    sys.exit(app.exec())
