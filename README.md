# monaco-qt

[![license](https://img.shields.io/pypi/l/monaco-qt.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/monaco-qt.svg)](https://pypi.org/project/monaco-qt/)
[![PyPI status](https://img.shields.io/pypi/status/monaco-qt.svg)](https://github.com/DaelonSuzuka/monaco-qt/)

The [monaco text editor](https://github.com/microsoft/monaco-editor) deployed as a Qt Widget.

Uses QWebEngineView to load a custom web page containing an instance of monaco.

# Installation

`pip install monaco-qt`

Then, in your qt application:

```py
from monaco import MonacoWidget

monaco_widget = MonacoWidget()
monaco_widget.setText('foo')
```

# Known Issues

- Pyinstaller doesn't automatically include the monaco typescript files.
- Very little of the monaco-editor API has been exposed to python so far
