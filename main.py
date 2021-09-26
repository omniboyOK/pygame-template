import pygame
from game.game import GameState
from game.constants import FPS, GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT

# General Setup
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)
pygame.font.init()

## Custom game manager
game_state = GameState(SCREEN)

## Game internal clock
clock = pygame.time.Clock()

## Pause conditional
run = True

while run:
    game_state.state_manager()
    clock.tick(FPS)
