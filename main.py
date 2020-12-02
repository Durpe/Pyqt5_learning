import sys
from ui.install import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = Ui_MainWindow()

    ui.show()
    sys.exit(app.exec_())