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

        # Options that indicate the movement of the rocket
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the rocket based on the option that indicates its movement"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Display of the rocket in its active position"""
        self.screen.blit(self.image, self.rect)
