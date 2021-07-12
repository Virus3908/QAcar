import pygame
from settings import *
from player import Player
import math
from map import *
from ray_casting import ray_casting
from drawing import Drawing
import sys

pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)
a=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    player.movement()
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos(), player.angle)
    drawing.fps(clock)

    #pygame.draw.circle(sc, GREEN, (int(player.x),int(player.y)), 12)
    #pygame.draw.line(sc, GREEN, player.pos(), (player.x + WIDTH*math.cos(player.angle), player.y + WIDTH*math.sin(player.angle)))

    #for x,y in world_map:
    #    pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 1)

    pygame.display.update()
    clock.tick(FPS)
