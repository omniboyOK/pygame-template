import pygame
import glob
import os

from game.constants.images import REDUCER


class ResourceManager():
    def __init__(self) -> None:
        self.resources = {}

    def preload(self):
        self.preload_images()

    def preload_images(self):
        resource = {}

        # default image
        resource['default'] = pygame.image.load(
            './game/assets/images/default.png').convert()

        for library_key in REDUCER:
            # Add the library to the temp resource dict
            resource[library_key] = {}
            for image_key in REDUCER[library_key]:
                # Add the image preloaded to the resource library
                resource[library_key][image_key] = pygame.image.load(
                    REDUCER[library_key][image_key]).convert()
        self.resources = resource

    def show_libraries(self):
        for key in self.resources:
            print(self.resources)

    def get_image(self, library, image):
        if library not in self.resources or image not in self.resources[library]:
            return self.resources['default']

        return self.resources[library][image]
