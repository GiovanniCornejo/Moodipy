from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UserSummary import Person
from PlaylistGUI import PlaylistPg
from screeninfo import get_monitors
import time

class LoadPg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Load Page"
        self.desktop = QApplication.desktop()
        self.left = 0
        self.top = 0
        self.width = 900
        self.height = 550
        self.initUI()

    def initUI(self):
        #set scaling factors
        self.sw = (self.width / 1000)
        self.sh = (self.height / 610)
        #Set window 
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #d4d4ff")
        #Loading bar widget
        self.loadingBar = QProgressBar(self)
        self.loadingBar.setStyleSheet("background-color: #d4d4ff")
        self.loadingBar.setGeometry(self.sw*400, self.sh*420, self.sw*200, self.sh*25)
        #Start button for loading bar
        self.startBtn = QPushButton("Start", self)
        self.startBtn.move(self.sw*453, self.sh*460)
        self.startBtn.clicked.connect(self.startProgressBar)
        self.mood_window()
        self.show()

    def mood_window(self):
        # Labels
        Person.setLabel(self, "Generate your", True, self.sw*390, self.sh*200, self.sw*220, self.sh*35, self.sw*19, "white", False, 'Segoe UI')
        Person.moodLabel = Person.setMoodLabel(Person, Person.currentmood)
        Person.setLabel(self, Person.moodLabel, True, self.sw*270, self.sh*260, self.sw*450, self.sh*58, self.sw*25, "white", True, 'Segoe UI')
        Person.setLabel(self, "Playlist", True, self.sw*385, self.sh*330, self.sw*220, self.sh*35, self.sw*19, "white", False, 'Segoe UI')
    
    #Draw_circle
    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(self.sw*270, self.sh*70, self.sw*450, self.sh*450)
        
    def startProgressBar(self):
        #Progress Bar time                                <== Start PlaylistGenerator.py
        for i in range(100):
            time.sleep(0.05)
            self.loadingBar.setValue(i)

        self.nextPg = PlaylistPg()
        self.nextPg.show()
        self.hide()
