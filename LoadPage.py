# fixing up, not done

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LoadPg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Load Page"
        self.left = 9
        self.top = 100
        self.width = 1000
        self.height = 610
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("background-color: #d4d4ff")
        self.mood_window()
        self.show()

    def mood_window(self):
        # Labels
        self.setLabel("Generating your", True, 390, 200, 220, 35, 19, "white", False)
        self.setLabel("Down", True, 380, 280, 230, 58, 35, "white", True)
        self.setLabel("Playlist", True, 390, 380, 220, 35, 19, "white", False)

    def paintEvent(self, event):
        paint = QPainter(self)
        paint.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        paint.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        paint.drawEllipse(270, 70, 450, 450)

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
