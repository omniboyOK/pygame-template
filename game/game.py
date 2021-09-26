from game.level_1 import Level1
from game.intro import IntroScreen
import pygame


class GameState():
    def __init__(self, screen, resources):
        self.screen = screen
        self.state = 'intro'
        self.font = pygame.font.SysFont(None, 48)
        self.resources = resources

    def set_state(self, state):
        self.state = state

    def state_manager(self):
        if self.state == 'intro':
            IntroScreen.run(self)
        if self.state == 'level1':
            Level1.run(self)
