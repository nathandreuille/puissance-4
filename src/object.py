import pygame

class Token:

    def __init__(self,color :int ,token_image : str):
        self.color = color
        self.token_image = token_image

    def load_token(self):
        token =  pygame.image.load(self.token_image).convert_alpha()
        return token



        
       