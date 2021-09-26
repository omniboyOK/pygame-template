from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
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
        manager.screen.fill('black')
        title_image = manager.font.render('INTRO SCREEN', True, 'Red')
        manager.screen.blit(title_image, (SCREEN_WIDTH /
                            2 - 100, SCREEN_HEIGHT / 2))
        pygame.display.update()

        pygame.display.flip()
