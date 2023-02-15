from graphics import *


#radius1 : raio do objeto 1
#radius2 : raio do objeto 2
#X1 : Coordenada X do objeto 1
#X2 : Coordenada X do objeto 2
#Y1 : Coordenada Y do objeto 1
#Y2 : Coordenada Y do objeto 2
def collided(radius1, radius2, X1 , X2 , Y1, Y2):
    return ( ( ( ( (int(X2-X1)) ** 2 ) + ( (int(Y2-Y1)) ** 2) ) ** 0.5) <= (int(radius1)) + (int(radius2)) )