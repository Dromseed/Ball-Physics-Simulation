import pygame.mixer

class Sound:
    def __init__(self, sound_file : str, volume : float):
        self.sound_file = sound_file
        self.sound = pygame.mixer.Sound(self.sound_file)
        self.volume = volume
    
    def play(self):
        self.sound.set_volume(self.volume)
        self.sound.play()