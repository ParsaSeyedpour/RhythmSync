import pygame

def load_and_play_sound(filepath):
    """Load and play a WAV sound file."""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(filepath)
    sound.play()
    return sound  # Return the sound object to check if it's still playing
