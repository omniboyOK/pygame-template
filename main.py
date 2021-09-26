import pygame
from game.game import GameState
from game.constants import FPS, GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT

# General Setup
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

## Custom game manager
game_state = GameState()

## Game internal clock
clock = pygame.time.Clock()

## Pause conditional
run = True

while run:
    game_state.state_manager()
    clock.tick(FPS)
