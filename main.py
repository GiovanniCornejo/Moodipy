import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UserSummary import Person
from MoodAnalyzerGUI import MoodAnalyzerPg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Moodipy"
        self.desktop = QApplication.desktop()
        self.left = 0
        self.top = 0
        self.width = self.desktop.width()-100
        self.height = self.desktop.height()-100
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #ffdb94")
        self.main_window()
        self.show()

    def main_window(self):
        print(self.width)
        print(self.height)
        button = QPushButton(self)
        button.setGeometry(self.width/2.08, self.height/1.36, self.width/25, self.height/30.5)
        button.setStyleSheet("border-image : url(imgs/arrow.png);")
        button.clicked.connect(self.next_page)
        Person.setLabel(self, "Welcome to", True, self.width / 2.56, self.height / 3.05, self.width / 4.55, self.height / 17.43, (self.width/1280)*19, "white", False, 'Consolas')
        Person.setLabel(self, "Moodipy", True, self.width/2.63, self.height/2.35, self.width/4.35, self.height/10.5, (self.width/1280)*35, "white", True, 'Segoe UI')
        Person.setLabel(self, "Generating playlists that express how you feel", True, self.width/2.99, self.height/1.63, self.width/2.99, self.height/30.5, (self.width/1280)*9, "white", False, 'Consolas')


    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(self.width/3.6875, self.height/10.3, self.width/2.22, self.width/2.22)

    def next_page(self):
        self.nextPg = MoodAnalyzerPg()
        self.nextPg.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
