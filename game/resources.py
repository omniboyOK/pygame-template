import pygame
import glob
import os


class ResourceManager():
    def __init__(self) -> None:
        self.resources = {}
        self.imagedir = './game/assets/images/'
        self.basedir = '/game/assets'
        self.resource_list = os.walk(self.imagedir)

    def preload(self):
        resource = {}
        for dirs in self.resource_list:
            for resource_folder in dirs[1]:
                asset_list = glob.glob(
                    self.imagedir + resource_folder + '/*.png')
                for asset in asset_list:
                    asset_name = os.path.splitext(os.path.basename(asset))[0]
                    resource[asset_name] = pygame.image.load(
                        asset).convert()

        self.resources[resource_folder] = resource

    def show_libraries(self):
        for key in self.resources:
            print(self.resources)

    def get_image(self, library, image):
        # TODO: Add a custom image when resource not found (if not library/image in resources)
        return self.resources[library][image]
