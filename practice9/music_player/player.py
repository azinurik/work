import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.tracks = [
            "/Users/nurdilda/work/practice9/music_player/music/track1.wav",
            "/Users/nurdilda/work/practice9/music_player/music/track2.wav"
        ]
        self.current = 0

    def play(self):
        pygame.mixer.music.load(self.tracks[self.current])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.current = (self.current + 1) % len(self.tracks)
        self.play()
        
    def prev(self):  
        self.current = (self.current - 1) % len(self.tracks)
        self.play() 