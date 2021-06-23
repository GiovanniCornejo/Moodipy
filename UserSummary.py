import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Person:
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__currentMood = []
        date = datetime.datetime.now().date()
        self.__moods = {}
        self.__moods[date] = self.__currentMood
        self.__userID = None


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def currentmood(self):
        return self.__currentMood

    @property
    def moods(self):
        return self.__moods

    @currentmood.setter
    def currentmood(self, currentMood):
        self.__currentMood = currentMood

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID):
        self.__userID = userID

    def setLabel(self, text, center, left, top, width, height, ftSize, bkColor, bold, font):
        label = QLabel(text, self)
        if center:
            label.setAlignment(Qt.AlignCenter)
        label.setGeometry(left, top, width, height)
        style = "background-color: "+bkColor+";"
        if bold:
            style = style+"font-weight: bold"
        label.setStyleSheet(style)
        label.setFont(QFont(font, ftSize))

