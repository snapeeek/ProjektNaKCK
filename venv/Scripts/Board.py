from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MyPushButton import MyPushButton
from enum import Enum

class Typ(Enum):
    PUSTE = 0
    BIALE = 1
    CZARNE = 2
    BIALAD = 3
    CZARNAD = 4

class Board:
    def __init__(self):
        super(Board, self).__init__()
        self.isPieceSelected = False
        self.board = []
        self.tempbutton = None
        self.initUI()

    def uncheckall(self):
        for i in range (0,8):
            self.grupy[i].setExclusive(False)
            for j in range(1,9):
                self.grupy[i].button(j).setChecked(False)
            self.grupy[i].setExclusive(True)


    def buttonpressed(self):
        for i in range (0,8):
            self.tempbutton = self.grupy[i].checkedButton()
            tempint = [i, self.grupy[i].checkedId()]
            if self.tempbutton is not None:
                break
        self.uncheckall()
        print(self.tempbutton.getKind())
        print("Wcisniety przycisk:", chr(ord('A') + tempint[0]), tempint[1])
        #self.updateboard([0,1,2,0,0,0,1,2,2,1,0,0,0,0,1,2,0,0,0,1,0,2,1,2,2,0,1,1,1,0,3,4])

    def updateboard(self, tablica):
        counter = 0
        if len(tablica) != 32:
            print("Tablica jest nie teges")
        else:
            for i in tablica:
                if (i == Typ.PUSTE):
                    self.goodbuttons[counter].setStyleSheet("background-color: gray")
                elif (i == Typ.BIALE):
                    self.goodbuttons[counter].setStyleSheet("background-image: url(białyzwykły50.jpg)")
                elif (i == Typ.CZARNE):
                    self.goodbuttons[counter].setStyleSheet("background-image: url(czarnyzwykły50.jpg)")
                elif (i == Typ.BIALAD):
                    self.goodbuttons[counter].setStyleSheet("background-image: url(białadama50.jpg)")
                elif (i == Typ.CZARNAD):
                    self.goodbuttons[counter].setStyleSheet("background-image: url(czarnadama50.jpg)")
                counter = counter + 1

    def startingBoard(self):
        for i in range (0,8):
            self.grupy.append(QButtonGroup())
            self.grupy[i].setExclusive(True)
        for i in range(0,8):
            for j in range(0,8):
                button = MyPushButton(0)
                button2 = QPushButton()
                button.setCheckable(True)
                if ((i+j)%2 == 1 and i >= 0 and i < 3):
                    button.setStyleSheet("background-image: url(białyzwykły50.jpg)")
                    button.setKind(1)
                    self.goodbuttons.append(button)
                elif ((i + j) % 2 == 1 and i >= 5 and i < 9):
                    button.setStyleSheet("background-image: url(czarnyzwykły50.jpg)")
                    button.setKind(2)
                    self.goodbuttons.append(button)
                elif ((i + j) % 2 == 1):
                    button.setStyleSheet("background-color: gray")
                    self.goodbuttons.append(button)
                else:
                    button.setStyleSheet("background-color: white")
                    button.setEnabled(False)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.grupy[i].addButton(button, j+1)
                self.grid.addWidget(button, i, j)

    def initUI(self):
        self.mainwidget = QWidget()
        self.mainwidget.setFixedSize(600,600)
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.mainwidget.setLayout(self.grid)
        self.grupy = []
        self.goodbuttons = []
        self.startingBoard()

        #print(self.grupy[1].button(1).getKind())
        self.mainwidget.show()

        self.grupy[0].buttonClicked.connect(self.buttonpressed)
        self.grupy[1].buttonClicked.connect(self.buttonpressed)
        self.grupy[2].buttonClicked.connect(self.buttonpressed)
        self.grupy[3].buttonClicked.connect(self.buttonpressed)
        self.grupy[4].buttonClicked.connect(self.buttonpressed)
        self.grupy[5].buttonClicked.connect(self.buttonpressed)
        self.grupy[6].buttonClicked.connect(self.buttonpressed)
        self.grupy[7].buttonClicked.connect(self.buttonpressed)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    board = Board()
    sys.exit(app.exec())