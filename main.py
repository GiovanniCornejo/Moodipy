import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UserSummary import Person
from UserLogin import UserLoginPG


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Moodipy"
        self.left = 9
        self.top = 100
        self.width = 1000
        self.height = 610
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #ffdb94")
        self.main_window()
        self.show()

    def main_window(self):
        button = QPushButton(self)
        button.setGeometry(480, 450, 40, 20)
        button.setStyleSheet("border-image : url(arrow.png);")
        button.clicked.connect(self.next_page)
        Person.setLabel(self, "Welcome to", True, 390, 200, 220, 35, 19, "white", False,'Consolas')
        Person.setLabel(self, "Moodipy", True, 380, 260, 230, 58, 35, "white", True, 'Segoe UI')
        Person.setLabel(self, "Generating playlists that express how you feel", True, 335, 375, 338, 20, 9, "white", False,'Consolas')


    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(270, 70, 450, 450)

    def next_page(self):                                    
        self.nextPg = MoodAnalyzerPg()
        self.nextPg.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

