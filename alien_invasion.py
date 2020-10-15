import sys
import pygame
from settings import Settings
from rocket import Rocket


class AlienInvasion:
    """General class dedicated to managing the resources and the way the game works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.scree_height))
        pygame.display.set_caption("Alien Invasion")

        self.rocket = Rocket(self)

    def run_game(self):
        """Starting the main game loop"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Reaction to events generated by the keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False

    def _update_screen(self):
        """Updates the images on the screen and goes to a new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Create a copy of the game and start it
    ai = AlienInvasion()
    ai.run_game()
