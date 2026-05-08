#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 128, 0]
BLEU = [0, 0, 255]
JAUNE = [255, 255, 0]
ROSE = [255, 192, 203]
AZURE = [0, 150, 255]
# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(ROSE)
    
    pygame.draw.rect(ecran, BLANC, [20,20, 100,20])
    pygame.draw.rect(ecran, BLEU, [20,40, 100,20])
    pygame.draw.rect(ecran, ROUGE, [20,60, 100,20])

    pygame.draw.rect(ecran, BLANC, [160,20, 100,60])
    pygame.draw.circle(ecran, ROUGE, [210,50], 20)

    pygame.draw.rect(ecran, NOIR, [280,20, 30,60])
    pygame.draw.rect(ecran, JAUNE, [310,20, 30,60])
    pygame.draw.rect(ecran, ROUGE, [340,20, 30,60])
    
    pygame.draw.rect(ecran, VERT, [400,20, 100,60])
    pygame.draw.circle(ecran, ROUGE, [450,50], 20)

    pygame.draw.rect(ecran, AZURE, [520,20, 100,30])
    pygame.draw.rect(ecran, JAUNE, [520,50,100,30])

    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()