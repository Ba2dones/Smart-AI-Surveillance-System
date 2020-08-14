from client import *
from Ui.Ui_Register import *
from Ui.Ui_Login import *
import sys

#Note : QMainWindow is just another widget imported from QtWidgets ;)
class Login(QMainWindow, Ui_Login):
    switch_window = QtCore.pyqtSignal()
    #switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
       QMainWindow.__init__(self)
       self.setupUi(self)
       self.RegButton.clicked.connect(self.btn_register_handler)
        #self.btn_Submit.clicked.connect(self.btn_submit_handler)

    def btn_register_handler(self):
        self.switch_window.emit()

class Register(QMainWindow, Ui_Register):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
       QMainWindow.__init__(self)
       self.setupUi(self)
       self.LoginButton.clicked.connect(self.back_handler)

    def back_handler(self):
        self.switch_window.emit()
        
class Controller:

    def __init__(self):
    
       #client=client('http://18.213.123.42',3500)
       pass

    def show_login_page(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_registeration_page)
        #self.login.switch_window1.connect(self.show_discovery)
        #super.close()
        self.login.show()

    def show_registeration_page(self):
        self.register = Register()
        self.register.switch_window.connect(self.show_login_page)
        self.login.close()
        self.register.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
