# qt-gruenhagen-browser

This is qt-gruenhagen-browser, a project I've started to create a web browser that suits my personal needs. It's built
on top of Qt for Python and Qt WebEngine. The goal is to learn and experiment with browser development, focusing on
UI/UX customization and managing cookies and local storage.

## Table of Contents

- [Project Goals](#project-goals)
  - [Features to Implement](#features-to-implement)
    - [High Priority Initial Features](#high-priority-initial-features)
    - [Additional Core Features](#additional-core-features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Browser](#running-the-browser)
- [Testing](#testing)
  - [Unit Tests](#unit-tests)
  - [Behavior Documentation Tests](#behavior-documentation-tests)
- [Feedback](#feedback)

## Project Goals

- **Personal Customization:** Tailor the browser's look and functionality to my personal preferences.
- **UI/UX Focus:** Experiment with different user interface and user experience designs.
- **Cookie and Storage Management:** Improve control over cookies and local data.

### Features to Implement

#### High Priority Initial Features

- [x] Address bar
- [ ] Forward and back buttons (including navigation history)
- [ ] Dev tools (will unlock more features to implement)

#### Additional Core Features

- [ ] Tabbed browsing
- [ ] Workspaces (groups of tabs)
- [ ] Bookmarks
- [ ] Browsing history
- [ ] Private browsing (by default) and profile management
- [ ] New profile for each tab by default, but with ability to link multiple tabs to a single profile
- [ ] Prompt to save tab/profile on close
- [ ] Prompt to open a new tab when navigating to a new domain
- [ ] Cookie management
- [ ] Local storage management
- [ ] Download manager
- [ ] Dark mode
- [ ] URL error handling in the address bar
- [ ] Search engine selection (I want to experiment with requiring manual selection of search engine for each search)
- [ ] Plugin support (manifest v2 and v3 -- not sure if this is feasible with QtWebEngine)
- [ ] Password manager (ideally BitWarden integration -- implementation depends on if plugin support is possible)
- [ ] Ad blocker (ideally uBlock Origin, if plugin support is possible)

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

## Testing

### Unit Tests

```ssh
poetry run pytest
```

### Behavior Documentation Tests

```ssh
poetry run pytest -m documenting_behavior
```
These tests document and demonstrate unusual behavior that is not intuitive to me as the developer. They are not
necessarily bugs or even directly related to the browser, but are intended to help me understand the behavior of the
the browser's underlying technologies.

## Feedback

While qt-gruenhagen-browser is a personal project tailored to my specific needs, I'm open to hearing your thoughts and
suggestions. If you have any feedback or ideas that might enhance the browser, feel free to share:

- **Feedback:** Any insights or suggestions to improve the browser are welcome.
- **Issues:** If you notice something not working as expected, let me know.

Your input is valuable, and I'm keen to hear diverse perspectives to refine this personal project further.

Thank you for taking the time to explore the qt-gruenhagen-browser!

-Malachi Gruenhagen, NurseTheCode
