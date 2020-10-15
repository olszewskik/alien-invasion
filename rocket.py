import pygame


class Rocket:
    """A class for rocket management"""

    def __init__(self, ai_game):
        """Initialization of the rocket and its position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image and retrieves its rectangle
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        # Each new rocket appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Display of the rocket in its active position"""
        self.screen.blit(self.image, self.rect)
