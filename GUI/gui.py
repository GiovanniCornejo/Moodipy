import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = 'Moodipy'
        self.left = 9
        self.top = 100
        self.width = 3820
        self.height = 1900
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.UiComponents()
        self.show()
        self.setStyleSheet("background-color: #ffdb94")

    def setLabel(self, text, center, left, top, width, height, ftSize, bkColor, bold):
        label = QLabel(text, self)
        if center:
            label.setAlignment(Qt.AlignCenter)
        label.setGeometry(left, top, width, height)
        style = "background-color: "+bkColor+";"
        if bold:
            style = style+"font-weight: bold"
        label.setStyleSheet(style)
        label.setFont(QFont('Segoe UI', ftSize))


    def UiComponents(self):
        button = QPushButton(self)
        button.setGeometry(1910, 1490, 130, 90)
        button.setStyleSheet("border-image : url(arrow.png);")
        #button.setStyleSheet("border-radius: 50; border :8px solid pink")
        button.clicked.connect(self.click1)

        self.setLabel("Welcome to", True, 1460, 500, 1000, 510, 30, "white", False)
        self.setLabel("Moodipy", True, 1460, 830, 1000, 260, 50, "white", True)
        self.setLabel("Generating playlists that express how you feel", True, 1460, 1200, 1000, 100, 12, "white", False)



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        painter.setBrush(QBrush(QBrush(Qt.white, Qt.SolidPattern)))
        painter.drawEllipse(1220, 180, 1500, 1500)


    def click1(self):
        print("dumdum")
        self.setWindowTitle("Mood Analyzer")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.UiComponents2()
        self.show()
        self.setStyleSheet("background-color: #8599ff")

    def UiComponents2(self):
        button2 = QPushButton(self)
        button2.setGeometry(1910, 1490, 130, 90)
        button2.setStyleSheet("border-image : url(arrow.png);")
        self.setLabel("How are you feeling?", False, 110, 110, 1000, 510, 40, "white", True)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
