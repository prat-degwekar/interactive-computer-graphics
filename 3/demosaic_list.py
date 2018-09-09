import numpy as np
import pygame
import random as ran

#bayerr = np.random.randint(0, high = 255, size = (100,60))
#bayerg = np.random.randint(0, high = 255, size = (100,60))
#bayerb = np.random.randint(0, high = 255, size = (100,60))
#bayerg = np.zeros((100,60))
#bayer = np.zeros((100,60))

l1 = [(x%2)*ran.randint(0,255) for x in range(0,10)]
l3 = [[(x%2)*ran.randint(0,255) for x in range(0,10)] for i in range(5)]
bayerr = [[((i%2)^1) * ((x%2)^1) * ran.randint(0,255) for x in range(0,60)] for i in range(100)]  #100x60 matrix

bayerg = [0]*100
bayerg1 = [[((i%2) ^ 1) * (x%2) * ran.randint(0,255) for x in range(0,60)] for i in range(100)]
bayerg2 = [[((i%2)^0)*((x%2)^1)*ran.randint(0,255) for x in range(0,60)] for i in range(100)]
'''for i in range(100):
    bayerg[i] = [((i%2) * [((i%2) ^ 1) * (x%2) * ran.randint(0,255) for x in range(0,60)] + ((i%2) ^ 1) * [((i%2)^0)*((x%2)^1)*ran.randint(0,255) for x in range(0,60)] )]'''
for i in range(100):
    if i%2 is 0:
        bayerg[i] = (bayerg1[i])
    else:
        bayerg[i] = (bayerg2[i])

bayerb = [[((i%2) ^ 0) * (x%2) * ran.randint(0,255) for x in range(0,60)] for i in range(100)]

bayer = [[[0] * 3 for i in range(60)] for j in range(100)]   #100x60x3 matrix
#bayer = [[[0]]]
#bayer = [[[... for i in range(60)] for j in range(100) ] for k in range(3) ]
#or make a 3x100x60 matrix for readability

'''for i in range (0,100):
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
'''

for i in range (100):
    for j in range(60):
        for k in range(3):
            if k is 0:
                bayer[i][j][k] = bayerr[i][j]
            elif k is 1:
                bayer[i][j][k] = bayerg[i][j]
            else:
                bayer[i][j][k] = bayerb[i][j]
        '''bayer[i][j][0].append(bayerr[i][j])
        bayer[i][j][1].append(bayerg[i][j])
        bayer[i][j][2].append(bayerb[i][j])'''

monitor = pygame.display.set_mode( (640, 400) )

try:
    
    #f = open('bayers.txt','w')
    with open('bay_list.txt', 'w') as f:
        for item in bayer:
            f.write("%s\n" % item)

finally:
    f.close()

#create rgb file

#r = g = b = np.zeros((100,60)) fix this!!!
r = [[0] * 60 for i in range(100)]
g = [[0] * 60 for i in range(100)]
b = [[0] * 60 for i in range(100)]

zeros = 0

for i in range(1,99):
    for j in range(1,59):
##        r[i,j] = int(((bayer[i-1,j-1] + bayer[i-1,j+1] + bayer[i+1,j-1] + bayer[i+1, j+1])/4)) if (i%2 == 1 and j%2 == 1) \
##                 else int(((bayer[i-1,j] + bayer[i+1,j])/2 )) if (i%2 == 1 and j%2 == 0) \
##                 else int(((bayer[i,j-1] + bayer[i,j+1])/2 )) if (i%2 == 0 and j%2 == 1) \
##                 else int(((bayer[i,j])))
        zeros = 0
        for k in range(i-1, i+1):
            for l in range(j-1, j+1):
                if bayer[k][l][0] is 0:
                    zeros += 1
                r[i][j]+=bayer[k][l][0]
        r[i][j] /= (9-zeros)
        r[i][j] = int(r[i][j])

for i in range(1,99):
    for j in range(1,59):        
        '''g[i,j] = int((( bayer[i-1 , j] + bayer[i , j-1] + bayer[i , j+1] + bayer[i+1 , j])/4)) if ( (i+j)%2 == 0) \
                 else int((( bayer[i-1 , j-1] + bayer[ i-1 , j+1 ] + bayer[ i+1 , j-1] + bayer[ i+1 , j+1 ] + bayer[ i , j ] ) / 5))'''
        zeros = 0
        for k in range(i-1, i+1):
            for l in range(j-1, j+1):
                if bayer[k][l][1] is 0:
                    zeros += 1
                g[i][j]+=bayer[k][l][1]
        g[i][j] /= (9-zeros)
        g[i][j] = int(g[i][j])

for i in range(1,99):
    for j in range(1,59):
        '''b[i,j] = ((( bayer[ i , j ] ))) if (i%2 == 1 and j%2 == 1) else ((( bayer[i , j-1] + bayer[i , j+1] )/2)) if (i%2 == 1 and j%2 == 0) \
                 else ((( bayer[i-1 , j] + bayer[i+1 , j] )/2)) if (i%2 == 0 and j%2 == 1) \
                 else ((( bayer[i-1 , j-1] + bayer[i-1 , j+1] + bayer[i+1 , j-1] + bayer[i+1 , j+1] )/4))'''
        zeros = 0
        for k in range(i-1, i+1):
            for l in range(j-1, j+1):
                if bayer[k][l][2] is 0:
                    zeros += 1
                b[i][j]+=bayer[k][l][2]
        b[i][j] /= (9-zeros)
        b[i][j] = int(b[i][j])

for i in range(1,99):
    for j in range(1,59):        
        if(i%10 == 0 and j%10 == 0):
            print(r[i-1][j-1] , g[i-1][j-1] , b[i-1][ j-1], sep=' ')

'''np.savetxt('red.txt', r, delimiter=',')
np.savetxt('green.txt', g, delimiter=',')
np.savetxt('blue.txt', b, delimiter=',')'''

'''for k in range(i-1, i+1):
    for l in range(j-1, j+1):
        if bayer[k][l][0] is 0:
            zeros++
        r[i][j]+=bayer[k][l][0]'''

with open('red_list.txt', 'w') as f:
    for item in r:
        f.write("%s\n" % item)

with open('green_list.txt', 'w') as f:
    for item in g:
        f.write("%s\n" % item)

with open('blue_list.txt', 'w') as f:
    for item in b:
        f.write("%s\n" % item)

on = True
while on:
    for i in range(0,100):
       for j in range(0,60):
            if(i%2 == 0):
                if(j%2 == 0):
                    monitor.set_at((i+10, j+10), (bayer[i][j][0], 0, 0))
                else:
                    monitor.set_at((i+10, j+10), (0, bayer[i][j][1], 0))
            
            else :
                if(j%2 == 0):
                    monitor.set_at((i+10, j+10), (0, bayer[i][j][1], 0))
                else:
                    monitor.set_at((i+10, j+10), (0, 0, bayer[i][j][2]))


    for i in range (0, 98):
        for j in range (0, 58):
            monitor.set_at( (i + 10 , j + 130) , (r[i][j] , 0 , 0) )
            monitor.set_at( (i + 120 , j + 130) , (0 , g[i][j] , 0) )
            monitor.set_at( (i + 230 , j + 130) , (0 , 0 , b[i][j]) )

    for i in range (0, 98) :
        for j in range (0, 58) :
            monitor.set_at( (i + 10 , j + 250 ) , (r[i][j] , g[i][j] , b[i][j]) )
                    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           on = False

    pygame.display.flip()
