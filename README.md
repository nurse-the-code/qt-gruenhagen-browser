# qt-gruenhagen-browser

This is qt-gruenhagen-browser, a project I've started to create a web browser that suits my personal needs. It's built
with Python and PyQt6, including pyqt6-webengine-qt6 for web content rendering. The goal is to learn and experiment with
browser development, focusing on UI/UX customization and managing cookies and local storage.

## Project Goals

- **Personal Customization:** Tailor the browser's look and functionality to personal preferences.
- **UI/UX Focus:** Experiment with different user interface and user experience designs.
- **Cookie and Storage Management:** Improve control over cookies and local data.

## Technologies

- **[Python:](https://www.python.org/)** The main programming language used.
- **[Poetry](https://python-poetry.org/):** A dependency management tool for Python projects.
- **[Qt](https://www.qt.io/):** A cross-platform application framework used for the browser's UI and to wrap Chromium.
  See the [QtWebEngine documentation](https://wiki.qt.io/QtWebEngine) for more information, including a brief discussion
  of the engine's relationship with Chromium.
- **[Qt for Python](https://doc.qt.io/qtforpython/):** A set of official Python bindings for the Qt application
  framework.

## Getting Started

To get the qt-gruenhagen-browser up and running on your local machine, follow these setup instructions. This project
uses Poetry for dependency management, so make sure you have Poetry installed before you proceed. If you're new to
Poetry, you can find installation instructions on the [Poetry documentation](https://python-poetry.org/docs/#installation)
page.

### Prerequisites

- Python 3.12
- Poetry

### Installation

1. **Clone the repository:**

   First, clone the repository to your local machine using Git:

   ```sh
   git clone https://github.com/nurse-the-code/qt-gruenhagen-browser.git
   cd qt-gruenhagen-browser
   ```

2. **Install dependencies:**

   Navigate to the project directory (if you haven't already) and use Poetry to install the dependencies:

   ```sh
   poetry install
   ```

   This command reads the `pyproject.toml` file and installs all the necessary packages.

### Running the Browser

To start the browser, run the main Python script:

```sh
poetry run python main.py
```

This command tells Poetry to run the `main.py` file in the environment where all dependencies have been installed.

### Feedback

While qt-gruenhagen-browser is a personal project tailored to my specific needs, I'm open to hearing your thoughts and
suggestions. If you have any feedback or ideas that might enhance the browser, feel free to share:

- **Feedback:** Any insights or suggestions to improve the browser are welcome.
- **Issues:** If you notice something not working as expected, let me know.

Your input is valuable, and I'm keen to hear diverse perspectives to refine this personal project further.

Thank you for taking the time to explore the qt-gruenhagen-browser!

-Malachi Gruenhagen, NurseTheCode
