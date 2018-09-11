import pygame
import math

monitor = pygame.display.set_mode( (640, 400) )

def levcurve(x, y, l, alpha, n):
     if n > 0 :
         l = l/1.414

         levcurve(x, y, l, (45 + alpha), n-1)

         x = x + l*math.cos(math.radians(45 + alpha))
         y = y + l*math.sin(math.radians(45 + alpha))

         levcurve(x, y, l, alpha-45, n-1)

     elif n is 0 :
         #line(x, y, x+l*math.cos(alpha), y+l*math.sin(alpha))
         pygame.draw.line(monitor, (255, 255, 255), (x, y), ( (x+l*math.cos(math.radians(alpha))), (y+l*math.sin(math.radians(alpha)))), 1)



levcurve(320, 100, 100, 90, 12)

on = True
while on:
     pygame.display.flip()
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
           on = False

pygame.quit()
