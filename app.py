from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel()
        image = QPixmap('D:\ALDERVINYLS\Doodles.ALDERVINYL\\cover art.png')
        label.setPixmap(image)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(MusicRect())
        layout.addWidget(MusicRect())
        layout.addWidget(MusicRect())

        container = QWidget()
        container.setLayout(layout)

        self.setStyleSheet("""
            #musicRect {
                border: 1px solid black;
            }
        """)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

class MusicRect(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('musicRect')
        layout = QHBoxLayout(self)

        label = QLabel()
        label.setText("alala")
        #label.setStyleSheet("border: 1px solid black")

        play_button = QPushButton('>')
        play_button.setMaximumSize(50, 50)
        play_button.clicked.connect(self.handleButton)

        layout.addWidget(label)
        layout.addWidget(play_button)

    def handleButton(self):
        print('Hello World')

class MusicRectList():
    def __init__(self):
        pass
        #yoy


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()