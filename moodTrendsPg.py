from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UserSummary import Person

class MoodTrends(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Mood Trends"
        self.left = 9
        self.top = 100
        self.width = 1000
        self.height = 610
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #bdffcc")
        self.mood_window()
        self.show()

    def mood_window(self):
        Person.setLabel(self, "Mood Analysis", False, 20, 10, 370, 39, 20, "#bdffcc", True, 'Segoe UI')
        Person.setLabel(self, "Your Current Mood", False, 25, 100, 370, 39, 12, "#bdffcc", True, 'Segoe UI')
        Person.setLabel(self, "Your Mood Trends", False, 470, 330, 370, 39, 12, "#bdffcc", True, 'Segoe UI')
        Person.setLabel(self, "", False, 20, 58, 225, 3, 0, "black", False, 'Segoe UI')
        Person.setLabel(self, "", False, 25, 150, 480, 170, 0, "white", False, 'Segoe UI')
        Person.setLabel(self, "", False, 470, 370, 480, 170, 0, "white", False, 'Segoe UI')
        mood = ''
        if len(Person.currentmood) == 1:
            mood = Person.currentmood[0]
        else:
            mood = Person.currentmood[0] + " and " + Person.currentmood[1]

        Person.setLabel(self, mood, False, 90, 280, 150, 20, 11, "white", False, 'Consolas')



