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

app = QApplication([])
window = Stats()
window.ui.show()
print('ss')
app.exec_()
