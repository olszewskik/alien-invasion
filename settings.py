class Settings:
    """The class designed to store all game settings"""

    def __init__(self):
        """Initializing the game settings"""
        # screen settings
        self.screen_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)

        # rocket settings
        self.rocked_speed = 15

        # bullet settings
        self.bullet_speed = 25
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
