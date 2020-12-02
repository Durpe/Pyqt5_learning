import sys
from PySide2.QtWidgets import QApplication,QLabel,QPushButton,QDialog,QLineEdit,QVBoxLayout
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl
from PySide2.QtCore import Slot

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.setWindowTitle(
            'my form'
        )
        self.initUi()

    def initUi(self):
        self.edit = QLineEdit('write my name here...')
        self.button = QPushButton('show Greetings')
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print('hello {}'.format(self.edit.text()))
if __name__ == '__main__':
    app = QApplication([])

    form = Form()
    form.show()

    sys.exit(app.exec_())