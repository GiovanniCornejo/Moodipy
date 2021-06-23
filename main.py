import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UserSummary import Person
from MoodAnalyzerGUI import MoodAnalyzerPg
from screeninfo import get_monitors


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Moodipy"
        self.desktop = QApplication.desktop()
        self.left = 0
        self.top = 0
        self.width = get_monitors()[0].width -100
        self.height = get_monitors()[0].height -100
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #ffdb94")
        self.main_window()
        self.show()

    def main_window(self):
        self.sw = (self.width/1000)
        self.sh = (self.height/610)
        button = QPushButton(self)
        button.setGeometry(self.sw*480, self.sh*450, self.sw*40, self.sh*20)
        button.setStyleSheet("border-image : url(imgs/arrow.png);")
        button.clicked.connect(self.next_page)
        Person.setLabel(self, "Welcome to", True, self.sw*390, self.sh*200, self.sw*220, self.sh*35, self.sw*19, "white", False,'Consolas')
        Person.setLabel(self, "Moodipy", True, self.sw*380, self.sh*260, self.sw*230, self.sh*58, self.sw*35, "white", True, 'Segoe UI')
        Person.setLabel(self, "Generating playlists that express how you feel", True, self.sw*335, self.sh*375, self.sw*338, self.sh*20, self.sw*9, "white", False,'Consolas')


    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(self.sw*270, self.sh*70, self.sw*450, self.sw*450)

    def next_page(self):
        self.nextPg = MoodAnalyzerPg()
        self.nextPg.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
