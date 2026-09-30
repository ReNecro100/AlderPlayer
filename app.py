import os

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

        config = Config('config.txt')
        music_rect_list = MusicRectList(config, 'Forever Young.ALDERVINYL')
        for rect in music_rect_list.music_rects:
            layout.addWidget(rect)

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
    def __init__(self, path, name):
        super().__init__()
        self.path = path
        self.name = name
        self.draw_widget()
    def draw_widget(self):
        self.setObjectName('musicRect')
        layout = QHBoxLayout(self)

        label = QLabel()
        label.setText(self.name)
        # label.setStyleSheet("border: 1px solid black")

        play_button = QPushButton('>')
        play_button.setMaximumSize(50, 50)
        play_button.clicked.connect(self.handleButton)

        layout.addWidget(label)
        layout.addWidget(play_button)
    def handleButton(self):
        print(self.path)

class MusicRectList:
    def __init__(self, config_object, vinyl_name):
        self.music_rects = []
        self.config_object = config_object
        self.vinyl_name = vinyl_name
        self.path = self.config_object.path_to_aldervinyls
        songs = self.get_songs()
        for song in songs:
            self.music_rects.append(MusicRect(f'{self.path}\\' + f'{self.vinyl_name}\\'+song, song))
    def get_songs(self):
        return [elem for elem in os.listdir(f'{self.path}\\' + self.vinyl_name) if elem[-4:] == '.mp3'] #elem[-4:] == '.png' or

class Config:
    def __init__(self, config_file):
        with open(config_file, "r", encoding="utf-8") as config:
            vinyl_name = config.readline().replace("\n", "").replace("CurrentAlderVinyl: ", "") + '.ALDERVINYL'
            path_to_aldervinyls = config.readline().replace("PathToAlderVinyls: ", "").replace("\n", "")
            volume = float(config.readline().replace("Volume: ", "").replace("\n", ""))
            small_window = bool(config.readline().replace("IsSmallWindow: ", "").replace("\n", ""))
        self.vinyl_name = vinyl_name
        self.path_to_aldervinyls = path_to_aldervinyls
        self.volume = volume
        self.small_window = small_window


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()