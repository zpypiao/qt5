import sys, os

os.chdir(sys.path[0])

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from func.add import func_add


from ui import Ui_MainWindow




class UI(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super(UI, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.add)



    def add(self):

        nu1 = self.lineEdit_2.text()
        nu2 = self.lineEdit_4.text()

        try:
            nu1 = float(nu1)
            nu2 = float(nu2)

            ans = func_add(nu1, nu2)

            self.lineEdit_6.setText(str(ans))
        except:
            QMessageBox.warning(self, 'Format Error', 'Please enter number only')









if __name__=='__main__':
    # 程序启动
    app = QApplication(sys.argv)

    # creat window and display
    window = UI()
    window.show()

    # fix
    sys.exit(app.exec_())