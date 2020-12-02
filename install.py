import json
from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
import requests
class Stats:

    def __init__(self):
        # 调用ui文件
        qfile = QFile('ui/install.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)
        self.ui.pushButton.clicked.connect(self.greetings)


    def greetings(self):
        #r = requests.get('http://www.4399.com')
        self.ui.plainTextEdit_2.clear()
        try:
            r = requests.get(self.ui.lineEdit.text())
            r.encoding = 'GBK'
            txt = r.headers
            txt = dict(txt)
            for k,v in txt.items():
                self.ui.plainTextEdit_2.insertPlainText(k)
                self.ui.plainTextEdit_2.insertPlainText(":" + v + "\n")
                #self.ui.plainTextEdit_2.insertPlainText('\n')
        except Exception as e:
            self.ui.plainTextEdit_2.clear()
            self.ui.plainTextEdit_2.insertPlainText(str(e))







if __name__ == '__main__':
    app = QApplication([])
    window = Stats()
    window.ui.show()

    app.exec_()
