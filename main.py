import pygame

# Créer la fenetre du jeu :

pygame.init()

# 1 : titre et résolution de la fenetre 

resolution = (692,590)
pygame.display.set_caption("Puissance 4")
window_screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
damier = pygame.image.load("damier.png")
damier.convert_alpha()
red_token = pygame.image.load("pion_rouge.png")
red_token.convert_alpha()
yellow_token = pygame.image.load("pion_jaune.png")
yellow_token.convert_alpha()

#2 : Boucle pour maintenir la fenetre ouverte 

lauched = True
while lauched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False
    window_screen.blit(damier,[0,0])
    window_screen.blit(red_token,[100,100])
    window_screen.blit(yellow_token,[200,200])
    
    
    
    pygame.display.flip()