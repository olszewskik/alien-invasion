import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing the single alien in the fleet"""

    def __init__(self, ai_game):
        """Alien initialization and definition of its initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien's image and define it
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Placing a new alien near the left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact horizontal foreign position
        self.x = float(self.rect.x)
