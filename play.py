from vert.main import *
from vert.singup import Ui_Dialog as Ui_Singup
from vert.Log import Ui_Dialog as Ui_Login
from vert.data import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

reg_data=Reg("Cred.db")

class Singup(QDialog,Ui_Singup):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.sing.clicked.connect(self.addusr)

    def addusr(self):
        name=self.name.text()
        password=self.pass2.text()
        contact=self.con.text()
        email=self.mail.text()
        reg_data.add(name,password,contact,email)
        print("Done!")
        self.close()

class Login(QDialog,Ui_Login):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.login.clicked.connect(self.checkval)
        self.sinup.clicked.connect(self.genUp)

    def checkval(self):
        username=self.user.text()
        password=self.passE.text()
        flag=reg_data.search(username,password)
        print(flag)

    def genUp(self):
        signobj=Singup()
        signobj.exec_()


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.checklogin()

    def checklogin(self):
        loginobj=Login()
        loginobj.exec_()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    w= MainWindow()
    w.show()
    sys.exit(app.exec_())



