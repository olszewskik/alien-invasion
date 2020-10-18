class GameStats:
    """Monitoring of statistical data in game"""

    def __init__(self, ai_game):
        """Initializing the statistics"""
        self.settings = ai_game.settings
        self.reset_status()

        # Run game in active state
        self.game_active = True

    def reset_status(self):
        """Initialization of statistics that may change during the game"""
        self.rocket_left = self.settings.rocket_limit
