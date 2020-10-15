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
            # Waiting for a key or mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Refresh the screen during each iteration of the loop
            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme()

            # Display the last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    # Create a copy of the game and start it
    ai = AlienInvasion()
    ai.run_game()
