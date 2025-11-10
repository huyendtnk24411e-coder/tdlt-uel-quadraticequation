from QuadraticEquation_MainWindow import Ui_MainWindow
from myultils import quadratic_equation


class QuadraticEquation_MainWindowEx(Ui_MainWindow):
    def setupUi(self, Mainwindow):
        super().setupUi(Mainwindow)
        self.MainWindow = Mainwindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSolution.clicked.connect(self.process_solution)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonClose.clicked.connect(self.process_close)
    def process_solution(self):
        a=float(self.lineEditA.text())
        b=float(self.lineEditB.text())
        c=float(self.lineEditC.text())
        result=quadratic_equation(a,b,c)
        self.lineEditResult.setText(result)
    def process_clear(self):
        self.lineEditA.setText("")
        self.lineEditB.setText("")
        self.lineEditC.setText("")
        self.lineEditResult.setText("")
        self.lineEditA.setFocus()
    def process_close(self):
        self.MainWindow.close()