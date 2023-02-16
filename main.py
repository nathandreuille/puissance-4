import pygame

# Créer la fenetre du jeu :

pygame.init()

# 1 : titre et résolution de la fenetre 

resolution = (640,480)
pygame.display.set_caption("Puissance 4")
window_screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

#2 : Boucle pour maintenir la fenetre ouverte 

lauched = True
while lauched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False