import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing the single alien in the fleet"""

    def __init__(self, ai_game):
        """Alien initialization and definition of its initial position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien's image and define it
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Placing a new alien near the left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storing the exact horizontal foreign position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
