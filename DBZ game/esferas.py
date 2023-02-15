
import random
from graphics import *

def esferas(win,contador,Xpersonagem):
    
    imagens = ['Esfera 1.png','Esfera 2.png',"Esfera 3.png",'Esfera 4.png','Esfera 5.png','Esfera 6.png','Esfera 7.png','Esfera 1.png'] 
    list = []
    circulos = [] 

    sorteioX_esfera = [random.randint(50,300), random.randint(500,750)]
    sorteioY_esfera = [random.randint(330,550)]
    X_esfera = random.choice(sorteioX_esfera)
    Y_esfera = random.choice(sorteioY_esfera)
    if contador == 7:
        X_esfera = 10000
        Y_esfera = 10000

    if Xpersonagem < 400 and X_esfera < 400:
        X_esfera = X_esfera + 300

    elif Xpersonagem > 400 and X_esfera > 400:
        X_esfera = X_esfera - 300

    esfera = Image(Point(X_esfera,Y_esfera), imagens[contador])
    esfera.draw(win)
    esfera_circle = Circle(Point(esfera.getAnchor().getX(), esfera.getAnchor().getY()), esfera.getWidth() / 2)
    #esfera_circle.draw(win)
    
    return esfera , esfera_circle



