from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 调用ui文件
        qfile = QFile('ui/stats.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)
        self.ui.pushButton.clicked.connect(self.greetings)
    def greetings(self):
        self.ui.plainTextEdit_2.insertPlainText(self.ui.lineEdit.text())
        #self.ui.plainTextEdit_2.
app = QApplication([])
window = Stats()
window.ui.show()
app.exec_()

if __name__ == '__main__':
    window = Stats()