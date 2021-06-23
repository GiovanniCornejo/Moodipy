from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moodTrendsPg import MoodTrends
from moodAnalyzer import find_mood
from UserSummary import Person


class MoodAnalyzerPg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Mood Analyzer"
        self.left = 9
        self.top = 100
        self.width = 1000
        self.height = 610
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color:#abbdff")
        self.mood_window()
        self.show()

    def mood_window(self):
        # Labels
        Person.setLabel(self,"How are you feeling?", False, 20, 10, 370, 39, 20, "#abbdff", True, 'Segoe UI')
        Person.setLabel(self,"Write about your day...", False, 120, 70, 300, 35, 15, "#abbdff", False, 'Segoe UI')
        Person.setLabel(self, "Find your mood", False, 670, 70, 300, 35, 15, "#abbdff", False, 'Segoe UI')
        Person.setLabel(self, "", False, 20, 58, 320, 3, 0, "black", False, 'Segoe UI')
        # Textbox
        self.text = QTextEdit(self)
        self.text.setGeometry(60, 100, 350, 450)
        self.text.setStyleSheet("border: 30px solid; border-radius:60px; background-color: #99acff; border-color: #99acff")
        self.text.setFont(QFont('Segoe UI', 11))
        # Block design
        boxDesign = QLabel(self)
        boxDesign.setGeometry(570, 100, 350, 450)
        boxDesign.setStyleSheet("border: 30px solid; border-radius:60px; background-color: #99acff; border-color: #99acff")
        # OR label
        orLabel = QLabel("OR", self)
        orLabel.setAlignment(Qt.AlignCenter)
        orLabel.setGeometry(460, 300, 60, 60)
        orLabel.setStyleSheet("border-radius: 30px; background-color: #99acff; border-color: #99acff; font-weight: bold")
        orLabel.setFont(QFont('Segoe UI', 12))
        # Text submit button
        btn1 = QPushButton("submit", self)
        btn1.clicked.connect(self.on_click)
        btn1.setGeometry(200, 500, 80, 20)
        btn1.setStyleSheet("background-color: #abbdff;border-radius:10px; ")
        # Mood slider
        mood_slider = QSlider(Qt.Horizontal, self)
        mood_slider.setRange(0, 5)
        mood_slider.setGeometry(630, 400, 250, 30)
        mood_slider.setFocusPolicy(Qt.NoFocus)
        mood_slider.setPageStep(1)
        mood_slider.valueChanged.connect(self.updateMood)
        mood_slider.setStyleSheet("background-color: #99acff;")
        # Mood image
        self.mood_img = QLabel(self)
        self.mood_img.setGeometry(690, 200, 130, 130)
        self.mood_img.setStyleSheet("border-image : url(imgs/awful.jpeg);background-color: #99acff;")
        # Mood label
        self.mood = QLabel('awful', self)
        self.mood.setGeometry(740, 350, 50, 30)
        self.mood.setMinimumWidth(80)
        self.mood.setStyleSheet("background-color: #99acff;")
        self.mood.setFont(QFont('Segoe UI', 11))
        # Mood submit button
        btn2 = QPushButton("submit", self)
        btn2.clicked.connect(self.on_click2)
        btn2.setGeometry(720, 500, 80, 20)
        btn2.setStyleSheet("background-color: #abbdff;border-radius:10px; ")

    def updateMood(self, value):
        moods = ["awful", "bad", "okay", "happy", "excited", "love"]
        self.mood_img.setStyleSheet("border-image : url(imgs/%s.jpeg);" % moods[value])
        self.mood.setText(moods[value])

    def on_click(self):
        Person.currentmood = find_mood(self.text.toPlainText())
        self.nextPg = MoodTrends()
        self.nextPg.show()
        self.hide()

    def on_click2(self):
        print("your mood: %s" % self.mood.text())
        Person.currentmood = self.mood.text()
        self.nextPg = MoodTrends()
        self.nextPg.show()
        self.hide()


