
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap

import sys
from ui.MusicRectList import MusicRectList


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel()
        image = QPixmap('D:\ALDERVINYLS\Doodles.ALDERVINYL\\cover art.png')
        label.setPixmap(image)

        layout = QVBoxLayout()
        layout.addWidget(label)

        player = QMediaPlayer()
        audioOutput = QAudioOutput()
        player.setAudioOutput(audioOutput)

        config = Config('config.txt')
        music_rect_list = MusicRectList(config, 'Forever Young.ALDERVINYL', player, audioOutput)
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