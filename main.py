from qtstrap import *
from monaco import MonacoWidget 

app = BaseApplication()
window = BaseMainWindow()

monaco = MonacoWidget()
monaco.setText('penis')
monaco.textChanged.connect(print)

with CVBoxLayout(window) as layout:
    layout.add(monaco)

window.show()

app.exec_()