from game.constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH
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
        manager.screen.fill('black')

        # drawing background
        back = manager.resources.get_image('backgrounds', 'grasslands')
        manager.screen.blit(back, (0, 0))

        # drawing title
        title_image = manager.font.render('LEVEL1', True, 'Red')
        manager.screen.blit(title_image, (SCREEN_WIDTH /
                            2 - 100, SCREEN_HEIGHT / 2))

        pygame.display.update()

        pygame.display.flip()
