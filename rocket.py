import pygame


class Rocket:
    """A class for rocket management"""

    def __init__(self, ai_game):
        """Initialization of the rocket and its position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image and retrieves its rectangle
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()

        # Each new rocket appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # The rocket's horizontal position is stored as a floating point number
        self.x = float(self.rect.x)

        # Options that indicate the movement of the rocket
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the rocket based on the option that indicates its movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocked_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocked_speed

        # Updating rect based on self.x.
        self.rect.x = self.x

    def blitme(self):
        """Display of the rocket in its active position"""
        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        """Place the rocket in the center at the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
