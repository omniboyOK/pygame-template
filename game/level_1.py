import pygame
import sys


class Level1():
    def run(manager):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # draw
        pygame.display.flip()
        # update
        pygame.display.update()
