import numpy as np
import pygame

bayerr = np.random.randint(0, high = 255, size = (100,60))
bayerg = np.random.randint(0, high = 255, size = (100,60))
bayerb = np.random.randint(0, high = 255, size = (100,60))
#bayerg = np.zeros((100,60))
bayer = np.zeros((100,60))

for i in range (0,100):
    for j in range (0, 60):
        if(i%2 == 0):
            if(j%2 == 0):
                bayer[i,j] = bayerr[i,j]
            else:
                bayer[i,j] = bayerg[i,j]

        else:
            if(j%2 == 0):
                bayer[i,j] = bayerg[i,j]
            else:
                bayer[i,j] = bayerb[i,j]

monitor = pygame.display.set_mode( (640, 400) )

try:
    
    f = open('bayers.txt','w')
    np.savetxt(f, bayer, delimiter=',')

finally:
    f.close()

#create rgb file

r = np.zeros((100,60))
g = np.zeros((100,60))
b = np.zeros((100,60))

for i in range(1,99):
    for j in range(1,59):
        r[i,j] = int(((bayer[i-1,j-1] + bayer[i-1,j+1] + bayer[i+1,j-1] + bayer[i+1, j+1])/4)) if (i%2 == 1 and j%2 == 1) \
                 else int(((bayer[i-1,j] + bayer[i+1,j])/2 )) if (i%2 == 1 and j%2 == 0) \
                 else int(((bayer[i,j-1] + bayer[i,j+1])/2 )) if (i%2 == 0 and j%2 == 1) \
                 else int(((bayer[i,j])))

for i in range(1,99):
    for j in range(1,59):        
        g[i,j] = int((( bayer[i-1 , j] + bayer[i , j-1] + bayer[i , j+1] + bayer[i+1 , j])/4)) if ( (i+j)%2 == 0) \
                 else int((( bayer[i-1 , j-1] + bayer[ i-1 , j+1 ] + bayer[ i+1 , j-1] + bayer[ i+1 , j+1 ] + bayer[ i , j ] ) / 5))

for i in range(1,99):
    for j in range(1,59):
        b[i,j] = ((( bayer[ i , j ] ))) if (i%2 == 1 and j%2 == 1) else ((( bayer[i , j-1] + bayer[i , j+1] )/2)) if (i%2 == 1 and j%2 == 0) \
                 else ((( bayer[i-1 , j] + bayer[i+1 , j] )/2)) if (i%2 == 0 and j%2 == 1) \
                 else ((( bayer[i-1 , j-1] + bayer[i-1 , j+1] + bayer[i+1 , j-1] + bayer[i+1 , j+1] )/4))

for i in range(1,99):
    for j in range(1,59):        
        if(i%10 == 0 and j%10 == 0):
            print(r[i-1,j-1] , g[i-1,j-1] , b[i-1, j-1], sep=' ')

np.savetxt('red.txt', r, delimiter=',')
np.savetxt('green.txt', g, delimiter=',')
np.savetxt('blue.txt', b, delimiter=',')

on = True
while on:
    for i in range(0,100):
       for j in range(0,60):
            if(i%2 == 0):
                if(j%2 == 0):
                    monitor.set_at((i+10, j+10), (bayer[i,j], 0, 0))
                else:
                    monitor.set_at((i+10, j+10), (0, bayer[i,j], 0))
            
            else :
                if(j%2 == 0):
                    monitor.set_at((i+10, j+10), (0, bayer[i,j], 0))
                else:
                    monitor.set_at((i+10, j+10), (0, 0, bayer[i,j]))


    for i in range (0, 98):
        for j in range (0, 58):
            monitor.set_at( (i + 10 , j + 130) , (r[i,j] , 0 , 0) )
            monitor.set_at( (i + 120 , j + 130) , (0 , g[i,j] , 0) )
            monitor.set_at( (i + 230 , j + 130) , (0 , 0 , b[i,j]) )

    for i in range (0, 98) :
        for j in range (0, 58) :
            monitor.set_at( (i + 10 , j + 250 ) , (r[i,j] , g[i,j] , b[i,j]) )
                    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           on = False

    pygame.display.flip()
