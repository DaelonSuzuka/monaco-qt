from qtpy.QtCore import QObject, Signal, Slot, Property, QUrl
from qtpy.QtWebEngineWidgets import * 
from qtpy.QtWebChannel import *
import os
import json


class BaseBridge(QObject):
    initialized = Signal()
    sendDataChanged = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.active = False
        self.queue = []

    def send_to_js(self, name, value):
        if self.active:
            data = json.dumps(value)
            self.sendDataChanged.emit(name, data)
        else:
            self.queue.append((name, value))

    @Slot(str, str)
    def receive_from_js(self, name, value):
        data = json.loads(value)
        self.setProperty(name, data)

    @Slot()
    def init(self):
        self.initialized.emit()
        self.active = True
        for name, value in self.queue:
            self.send_to_js(name, value)

        self.queue.clear()


class EditorBridge(BaseBridge):
    valueChanged = Signal()
    languageChanged = Signal()
    themeChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._value = ""
        self._language = ""
        self._theme = ""

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
        self.valueChanged.emit()

    def getLanguage(self):
        return self._language

    def setLanguage(self, language):
        self._language = language
        self.languageChanged.emit()

    def getTheme(self):
        return self._theme

    def setTheme(self, theme):
        self._theme = theme
        self.themeChanged.emit()

    value = Property(str, fget=getValue, fset=setValue, notify=valueChanged)
    language = Property(
        str, fget=getLanguage, fset=setLanguage, notify=languageChanged
    )
    theme = Property(str, fget=getTheme, fset=setTheme, notify=themeChanged)


class MonacoWidget(QWebEngineView):
    textChanged = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIR, "index.html")
        self.load(QUrl.fromLocalFile(filename))

        channel = QWebChannel(self)
        self.page().setWebChannel(channel)

        self._bridge = EditorBridge()
        channel.registerObject("bridge", self._bridge)

        self._bridge.valueChanged.connect(lambda: self.textChanged.emit(self._bridge.value))

    def text(self):
        return self._bridge.value

    def setText(self, text):
        self._bridge.send_to_js("value", text)

    def language(self):
        return self._bridge.language

    def setLanguage(self, language):
        self._bridge.send_to_js("language", language)