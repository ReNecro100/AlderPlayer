from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from ui.MusicRectState import MusicRectState

class MusicRect(QWidget):
    def __init__(self, path, name, player, audioOutput, state):
        super().__init__()
        self.path = path
        self.name = name
        self.player = player
        self.audioOutput = audioOutput
        self.draw_widget()
        self.state = state
    def draw_widget(self):
        self.setObjectName('musicRect')
        layout = QHBoxLayout(self)

        label = QLabel()
        label.setText(self.name)
        # label.setStyleSheet("border: 1px solid black")


        self.play_button = QPushButton('>')
        self.play_button.setMaximumSize(50, 50)
        self.play_button.clicked.connect(self.handleButton)

        layout.addWidget(label)
        layout.addWidget(self.play_button)
    def handleButton(self):
        if self.state == MusicRectState.STOP:
            self.play_button.setText('||')
            self.player.setSource(QUrl.fromLocalFile(self.path))
            self.audioOutput.setVolume(0.5)
            self.player.play()
            self.state = MusicRectState.PLAY
        elif self.state == MusicRectState.PLAY:
            self.state = MusicRectState.PAUSE
            self.play_button.setText('>')
            self.player.pause()
        elif self.state == MusicRectState.PAUSE:
            self.state = MusicRectState.PLAY
            self.play_button.setText('||')
            self.player.play()
        #self.player.stop()
        print(self.path)