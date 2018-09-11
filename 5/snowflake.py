import pygame
import math

monitor = pygame.display.set_mode( (640, 400) )

def kochcurve(x, y, l, alpha, n):
     if n > 0 :

         l = l/3

         pygame.draw.line(monitor, (255, 255, 255), (x, y), ( (x + (l * 3) * math.cos(math.radians(alpha))), (y + ( l * 3) * math.sin(math.radians(alpha)))), 1)

         #first third (1/3) of original lines

         kochcurve(x, y, l, alpha, n-1)
         

         xd = ( x + (l) * math.cos(math.radians(alpha)))
         yd = ( y + (l) * math.sin(math.radians(alpha)))

         pygame.draw.line(monitor, (0, 0, 0), (xd, yd), ( (xd + ( l ) * math.cos(math.radians(alpha))), (yd + ( l ) * math.sin(math.radians(alpha)))), 3)

         #first of the second third (2/3 - line 1) of new lines

         kochcurve( xd, yd, (l), (alpha + 60), n-1)
         

         xt = xd + (l) * math.cos(math.radians(alpha + 60))
         yt = yd + (l) * math.sin(math.radians(alpha + 60))

         #second of the second third (2/3 - line 2) of new lines

         kochcurve(xt, yt, (l), alpha - 60, n-1)

         #third third (3/3) of original line

         xd = ( x + (2 * l) * math.cos(math.radians(alpha)))
         yd = ( y + (2 * l) * math.sin(math.radians(alpha)))

         kochcurve(xd, yd, l, alpha, n-1)

     elif n is 0 :
         
         pygame.draw.line(monitor, (255, 255, 255), (x, y), ( (x+l*math.cos(math.radians(alpha))), (y+l*math.sin(math.radians(alpha)))), 1)



length = 200
startx = 220
starty = 100

iterations = 5

kochcurve(startx, starty, length, 60, iterations)
kochcurve(startx + length, starty, length, 180, iterations)
kochcurve(startx + (length * math.cos(math.radians(60))), starty + (length * math.sin(math.radians(60))), length, 300, iterations)

on = True
while on:
     pygame.display.flip()
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
           on = False

pygame.quit()
