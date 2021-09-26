from game.level_1 import Level1
from game.intro import IntroScreen
import pygame
import sys


class GameState():
    def __init__(self) -> None:
        self.state = 'intro'

    def set_state(self, state):
        self.state = state

    def state_manager(self):
        if self.state == 'intro':
            IntroScreen.run(self)
        if self.state == 'level1':
            Level1.run(self)
