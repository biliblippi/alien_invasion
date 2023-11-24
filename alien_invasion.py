import sys
import pygame

from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()       # initialize the game, and create game resources
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_width, self.settings.screen_height)
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):     # start the main loop for the game
        while True:         # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)         # redraw the screen during each pass through the loop

            pygame.display.flip()       # make the most recently drawn screen visible

if __name__ == '__main__': 
    ai = AlienInvasion()        # make a game instance, and run the game
    ai.run_game()
    