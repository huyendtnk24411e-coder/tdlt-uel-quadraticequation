from PyQt6.QtWidgets import QApplication, QMainWindow

from QuadraticEquation_MainWindowEx import QuadraticEquation_MainWindowEx

app=QApplication([])
my_gui=QuadraticEquation_MainWindowEx()
my_gui.setupUi(QMainWindow())
my_gui.showWindow()
app.exec()