from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UserSummary import Person
from MoodAnalyzerGUI import MoodAnalyzerPg

class UserLoginPG(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.left = 9
        self.top = 100
        self.width = 1000
        self.height = 610
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #ccccff")
        #self.setStyleSheet("color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ccccff, stop:1 rgb(240, 53, 218));")
        self.mood_window()
        self.show()

    def mood_window(self):
        Person.setLabel(self, "", True, 290, 100, 460, 400, 0, "#f2ccff", False, 'Consolas')
        Person.setLabel(self, "Log In", False, 470, 130, 100, 39, 20, "#f2ccff", True, 'Consolas')
        Person.setLabel(self, "Login here using your Spotify username and password", False, 350, 170, 350, 39, 8, "#f2ccff", False, 'Consolas')
        Person.setLabel(self, "Username", False, 380, 230, 100,30,13, "#f2ccff", False, 'Consolas')
        Person.setLabel(self, "Password", False, 380, 290, 100, 30, 13, "#f2ccff", False, 'Consolas')
        self.username = QLineEdit(self)
        self.username.setGeometry(380, 260, 270, 29)
        self.username.setStyleSheet("background-color: white")

        self.password = QLineEdit(self)
        self.password.setGeometry(380, 320, 270, 29)
        self.password.setStyleSheet("background-color: white")

        loginbtn = QPushButton("LOGIN", self)
        loginbtn.setGeometry(450, 380, 150, 40)
        loginbtn.setStyleSheet("color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ccccff, stop:1 rgb(240, 53, 218)); border-style: solid; border-radius:20px;")
        loginbtn.clicked.connect(self.on_click)

    def on_click(self):
        Person.username = (self.username.text())
        Person.password = (self.password.text())
        self.nextPg = MoodAnalyzerPg()
        self.nextPg.show()
        self.hide()





