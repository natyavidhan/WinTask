from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
import json
import sys
table = ""

cluster = MongoClient('mongodb+srv://Studous_gamer:ilovemymommy@cluster0.oeo70.mongodb.net/Accounts?retryWrites=true&w=majority')
db = cluster['Accounts']
acc_table = db['Accounts']

cluster = MongoClient('mongodb+srv://Studous_gamer:ilovemymommy@cluster0.oeo70.mongodb.net/Lists?retryWrites=true&w=majority')
lists = cluster['Lists']
import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\\Users\\%s\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


class Ui_MainWindow(object):
    def logout_func(self):
        Details = {"Username": "", 
        "Password": "", 
        "table": ""}

        with open("Data/Data.json","w") as i:
            json.dump(Details,i)

        self.window = QtWidgets.QMainWindow()
        self.ui = logsign_ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def additem(self):
        global table
        if self.item_to_add.toPlainText() == "":
            return True
        else:
            self.noot_done_list.addItem(self.item_to_add.toPlainText())
            task_table = lists[table]
            task_table.insert_one({
                "type": "incomplete",
                "task": self.item_to_add.toPlainText()
            })
            self.item_to_add.setText("")

    def work_done(self):
            items = self.noot_done_list.selectedItems()
            if not items: return
            else:
                for item in items:
                    self.noot_done_list.takeItem(self.noot_done_list.row(item))
                    task_table = lists[table]
                    task_table.delete_one({"type":"incomplete",
                    "task":item.text()})
                    self.done_list.addItem(item.text())
                    task_table.insert_one({
                        "type":"complete",
                        "task":item.text()
                    })
    
    def removeSel(self):
        items = self.done_list.selectedItems()
        if not items: 
            return
        else:
            for item in items:
                self.done_list.takeItem(self.done_list.row(item))
                task_table = lists[table]
                task_table.delete_one({"type":"complete", "task":item.text()})

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('images/icon.png'))
        MainWindow.resize(510, 330)
        MainWindow.setMinimumSize(QtCore.QSize(510, 330))
        MainWindow.setMaximumSize(QtCore.QSize(510, 330))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(390, 240, 111, 31))
        self.done.setObjectName("done")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 230, 29, 79))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(270, 250, 101, 31))
        self.add.setObjectName("add")
        self.item_to_add = QtWidgets.QTextEdit(self.centralwidget)
        self.item_to_add.setGeometry(QtCore.QRect(10, 250, 251, 31))
        self.item_to_add.setObjectName("item_to_add")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 300, 501, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 310, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(390, 270, 111, 31))
        self.remove.setObjectName("remove")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 60, 501, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 491, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.noot_done_list = QtWidgets.QListWidget(self.layoutWidget)
        self.noot_done_list.setObjectName("noot_done_list")
        self.gridLayout.addWidget(self.noot_done_list, 1, 0, 1, 1)
        self.done_list = QtWidgets.QListWidget(self.layoutWidget)
        self.done_list.setObjectName("done_list")
        self.gridLayout.addWidget(self.done_list, 1, 1, 1, 1)
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(420, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(14)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.add.clicked.connect(self.additem)
        self.done.clicked.connect(self.work_done)
        self.remove.clicked.connect(self.removeSel)
        self.logout.clicked.connect(self.logout_func)
        self.logout.clicked.connect(MainWindow.hide)


        global table
        task_table = lists[table]
        results = task_table.find({"type":"incomplete"})
        for result in results:
            self.noot_done_list.addItem(result["task"])
        results = task_table.find({"type":"complete"})
        for result in results:
            self.done_list.addItem(result["task"])

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WinTask"))
        self.done.setText(_translate("MainWindow", "Complete Selected"))
        self.label.setText(_translate("MainWindow", "WinTask"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.label_2.setText(_translate("MainWindow", "©Studious Gamer"))
        self.remove.setText(_translate("MainWindow", "Remove Selected"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Incomplete</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Complete</p></body></html>"))
        self.logout.setText(_translate("MainWindow", "Logout"))

class Ui_SignUp(object):
    def addacc(self):
        global table 
        table = f'{self.lineEdit.text()}&{self.lineEdit_2.text()}'
        table = table.replace(" ", "")
        Details = {
            "Username": self.lineEdit.text(),
            "Password": self.lineEdit_2.text(),
            "table": table
        }
        
        if self.lineEdit.text() == "":
            return True
        elif self.lineEdit_2.text() == "":
            return True
        else:        
            with open("Data/Data.json","w") as i:
                json.dump(Details, i)
            acc_table.insert_one(Details)
            self.label_4.setText("Sucsessful! Now you can close this window")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")

    def setupUi(self, SIgnUp):
        SIgnUp.setMinimumSize(QtCore.QSize(350, 450))
        SIgnUp.setMaximumSize(QtCore.QSize(350, 450))
        SIgnUp.setObjectName("SIgnUp")
        SIgnUp.resize(350, 450)
        SIgnUp.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(SIgnUp)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 260, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 150, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 200, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        SIgnUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SIgnUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        SIgnUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SIgnUp)
        self.statusbar.setObjectName("statusbar")
        SIgnUp.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.addacc)
        self.pushButton.clicked.connect(MainWindow.hide)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 331, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(SIgnUp)
        QtCore.QMetaObject.connectSlotsByName(SIgnUp)

    def retranslateUi(self, SIgnUp):
        _translate = QtCore.QCoreApplication.translate
        SIgnUp.setWindowTitle(_translate("SIgnUp", "Sign Up"))
        self.label.setText(_translate("SIgnUp", "<html><head/><body><p align=\"center\">SIGN UP</p></body></html>"))
        self.pushButton.setText(_translate("SIgnUp", "Sign Up"))
        self.label_2.setText(_translate("SIgnUp", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Username</span></p></body></html>"))
        self.label_3.setText(_translate("SIgnUp", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Password</span></p></body></html>"))

class login_ui(object):
    def find_and_login(self):
        results = acc_table.find({"Username":self.lineEdit.text(),"Password":self.lineEdit_2.text()})
        for result in results:
            Details = {
            "Username": self.lineEdit.text(),
            "Password": self.lineEdit_2.text(),
            "table": result["table"]
            }
            with open("Data/Data.json","w") as i:
                json.dump(Details, i)
            global table
            table = result["table"]
            self.label_4.setText("Sucsessful! Now you can close this window")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
        if results == None:
            self.label_4.setText("Wrong Username or Password")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(350, 450))
        MainWindow.setMaximumSize(QtCore.QSize(350, 450))
        MainWindow.resize(350, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 150, 61))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 200, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 150, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 260, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.find_and_login)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 370, 331, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LOGIN</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Username</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Password</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

class logsign_ui(object):
    def open_login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = login_ui()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_signup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(341, 450))
        MainWindow.setMaximumSize(QtCore.QSize(341, 450))
        MainWindow.resize(341, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 301, 371))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(420, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Acme")
        font.setPointSize(14)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.open_login)
        self.pushButton.clicked.connect(MainWindow.hide)
        self.pushButton_2.clicked.connect(self.open_signup)
        self.pushButton_2.clicked.connect(MainWindow.hide)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WinTask"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">By Studious Gamer</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">WinTask</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Signup"))

if __name__ == "__main__":
    with open("Data/Data.json","r") as i:
        user = json.load(i)
    table = user["table"]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    if user["Username"] == "":
        ui = logsign_ui()
    else:
        ui = Ui_MainWindow()
    add_to_startup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    