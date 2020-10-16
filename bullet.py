import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class dedicated to manage bullets"""

    def __init__(self, ai_game):
        """Creation of a bullet object at the current rocket position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a projectile rectangle at point (0,0) and then define the appropriate position for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.rocket.rect.midtop

        # Bullet position is defined by a floating point value
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet on the screen"""
        # Bullet position update"""
        self.y -= self.settings.bullet_speed
        # Updating the position of the bullet rectangle"""
        self.rect.y = self.y

    def draw_bullet(self):
        """Display the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)