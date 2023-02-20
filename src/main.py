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
x = 0
y =0
x2=100
y2= 100
lauched = True
while lauched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False
    window_screen.blit(damier,[0,0])
    window_screen.blit(yellow_token,(x,y))
    window_screen.blit(red_token,(x2,y2))
    pressed = pygame.key.get_pressed()
    if pressed [pygame.K_LEFT]:
        x-=1
        
    if pressed [pygame.K_RIGHT]:
        x+=1
        
    if pressed [pygame.K_UP]:
        y-=1
        
    if pressed [pygame.K_DOWN]: 
        y+=1
        
    
        
    if pressed [pygame.K_q]:
        x2-=1
        
    if pressed [pygame.K_d]:
        x2+=1
        
    if pressed [pygame.K_z]:
        y2-=1
        
    if pressed [pygame.K_s]: 
        y2+=1
    
    pygame.display.flip()

    

    
    

    
"""
class Game :
    def __init__(self,age,poids):
        self.age = age
        self.poids = poids
    
    def afficher(self):
        print("j'ai",self.age,"et je fais",self.poids)
"""
