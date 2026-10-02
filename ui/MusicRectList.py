import os
from ui.MusicRect import MusicRect
from ui.MusicRectState import MusicRectState

class MusicRectList:
    def __init__(self, config_object, vinyl_name, player, audioOutput):
        self.music_rects = []
        self.config_object = config_object
        self.vinyl_name = vinyl_name
        self.path = self.config_object.path_to_aldervinyls
        self.player = player
        self.audioOutput = audioOutput
        songs = self.get_songs()
        for song in songs:
            self.music_rects.append(
                MusicRect(
                    f'{self.path}\\' + f'{self.vinyl_name}\\'+song,
                    song, self.player, self.audioOutput, MusicRectState.STOP))
    def get_songs(self):
        return [elem for elem in os.listdir(f'{self.path}\\' + self.vinyl_name) if elem[-4:] == '.mp3'] #elem[-4:] == '.png' or