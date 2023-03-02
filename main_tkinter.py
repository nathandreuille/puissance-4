import pygame
#from object import Token 


pygame.init()

# titre et résolution de la fenetre 

resolution = (692,590)
pygame.display.set_caption("Puissance 4")
window_screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

# damier puissance 4

checkerboard = pygame.image.load("image\damier.png").convert_alpha()

# création jetons rouges et jaunes



red_token = pygame.image.load("image\pion_rouge.png").convert_alpha()

yellow_token = pygame.image.load("image\pion_jaune.png").convert_alpha()
# reglage des frames 

clock = pygame.time.Clock()
x = 0
y =0
x2=100
y2= 100

#Boucle pour maintenir la fenetre ouverte 

lauched = True
while lauched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False
    
    clock.tick(240) #réglage des frames
    
    window_screen.blit(checkerboard,(0,0)) # affficher les images et leurs permettre de se déplacer
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

    

    
    

