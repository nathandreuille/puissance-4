import pygame

class Token:

    def __init__(self,color :int ,token_image : str):
        self.color = color
        self.token_image = token_image

    def load_token(self):
        token =  pygame.image.load(self.token_image)
        token.convert_alpha()


class Checkerboard :
    def __init__(self,checkerboard_image):
        self.checkerboard_image = checkerboard_image

    def load_checkerboard(self):
        checkerboard    = pygame.image.load(self.checkerboard_image)
        checkerboard.convert_alpha()