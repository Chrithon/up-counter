from PyQt5 import QtCore, QtGui, QtWidgets
from counter_gui import Ui_MainWindow
import sys

if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    QtCore.QCoreApplication.instance().quit
    sys.exit(app.exec_())
