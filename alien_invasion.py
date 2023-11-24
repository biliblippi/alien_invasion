import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()       # initialize the game, and create game resources
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion by biliblippi")

        self.ship = Ship(self)


    def run_game(self):     # start the main loop for the game
        while True:         # watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    
    def _check_events(self):
        '''respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        '''Update images on the screen and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)         
        self.ship.blitme()

        pygame.display.flip()       # make the most recently drawn screen visible



if __name__ == '__main__': 
    ai = AlienInvasion()        # make a game instance, and run the game
    ai.run_game()
    