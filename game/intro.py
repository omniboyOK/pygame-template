import pygame
import sys


class IntroScreen():
    def run(manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                manager.set_state('level1')

        # draw
        pygame.display.flip()
        # update
        pygame.display.update()
