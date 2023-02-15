from graphics import *
from esferas import *
from collided import *
import random

winWidth = 800
winHeight = 600
win = GraphWin("Take Goku",winWidth,winHeight)

key = 0

#tela de abertura
home_screen = Image(Point(winWidth/2,winHeight/2),"telaInicial.png")
home_screen.draw(win)



#função para qualquer mensagem
def message(X,Y,message,win,size,cor):
    message5 = Text(Point(X , Y),message)
    message5.setFill(cor)
    message5.setSize(size)
    message5.setFace("courier")
    message5.setStyle("bold")
    message5.draw(win)
    return message5



message(424,380,"Welcome to the game!",win,33,"gold")


gokuhead = Image(Point(90,480), "gokuhead.png")
gokuhead.draw(win)
message(35,490,'1',win,20,"gold")


goku4head = Image(Point(310,480), "goku4.png")
goku4head.draw(win)
message(250 , 488,"2",win,20,"gold")


gotenhead = Image(Point(100,550), "gotenhead.png")
gotenhead.draw(win)
message(35 , 560, "3" , win,20,"gold")


vegetahead = Image(Point(310 , 550), "vegetahead.png")
vegetahead.draw(win)
message(250,560,"4",win,20,"gold")


piccolohead = Image(Point(500 , 488), "piccolohead.png")
piccolohead.draw(win)
message(450,488,"5",win,20,"gold")


curirimhead = Image(Point(500 , 560), "curirimhead.png")
curirimhead.draw(win)
message(450,560,"6",win,20,"gold")


contador = 0


#"menu" para o jogador escolher o persogem que deseja jogar
while key != '1' and key != '2' and key != '3' and key != '4' and key != '5' and key != '6' and key != "Escape":
        key = win.checkKey()
        if key == '1':
            charr = "goku2.png"
        elif key == '2':
            charr = "saiyajin4.png"
        elif key == '3':
            charr = "goten.png"
        elif key == '4':
            charr = "vegeta.png"
        elif key == '5':
            charr = "piccolo.png"
        elif key == '6':
            charr = "curirim.png"
        elif key == "Escape":
            break


#Assim que o jogador escolher o personagem retira-se da tela 
message,vegetahead,goku4head,gotenhead,gokuhead.undraw()


character = Image(Point(400,160), charr)
colisao = 0


while key != 'Escape':
    #cenário de fundo do jogo
    scenery = Image(Point(winWidth/2,winHeight/2),"scenery (1).png")
    scenery.draw(win)


    #capsula e seu círculo
    capsule = Image(Point(180,224),"capsula12.png")
    capsule.draw(win)
    capsulaWidth = capsule.getWidth()
    capsuleCircle = Circle(Point(capsule.getAnchor().getX() , capsule.getAnchor().getY()), (capsulaWidth/2))


    #casa do céu e seu círculo
    casaCeu = Image(Point(730,60),"casaCeu.png")
    casaCeu.draw(win)
    casaCeuWidth = casaCeu.getWidth()
    casaCircle = Circle(Point(casaCeu.getAnchor().getX() , casaCeu.getAnchor().getY()),(casaCeuWidth/2 ) )

    
    #personagem e seu raio 
    character.draw(win)
    characterHeight = character.getHeight()
    character_circle = Circle(Point(character.getAnchor().getX(),character.getAnchor().getY()),(characterHeight/2))


    #inimigo e seu círculo em volta
    freezadrawed = 0
    freeza = Image(Point(100,250),"freeza1.png")
    freezaHeight = freeza.getHeight()
    freeza_circle = Circle(Point(freeza.getAnchor().getX(),freeza.getAnchor().getY()),(freezaHeight/3))
    freeza_radius = freeza_circle.getRadius()
    freezaX = freeza_circle.getCenter().getX()
    freezaY = freeza_circle.getCenter().getY()
    

    #inimigo e seu círculo em volta
    celldrawed = 0
    cell = Image(Point(700,200),"cell.png")
    cellHeight = cell.getHeight()
    cell_circle = Circle(Point(cell.getAnchor().getX(), cell.getAnchor().getY()),(cellHeight/2))
    cell_radius = cell_circle.getRadius()
    cellX = cell_circle.getCenter().getX()
    cellY = cell_circle.getCenter().getY()


    #inimigo e seu círculo em volta
    madimbudrawed = 0
    madimbu = Image(Point(310,150),"madimbu.png")
    madimbuHeight = madimbu.getHeight()
    madimbu_circle = Circle(Point(madimbu.getAnchor().getX(), madimbu.getAnchor().getY()),(madimbuHeight/4))
    madimbu_radius = madimbu_circle.getRadius()
    madimbuX = madimbu_circle.getCenter().getX()
    madimbuY = madimbu_circle.getCenter().getY()



    #função para o inimigo perseguir o persnagem
    def enemy_follow(enemy, enemyX , inimigoY , enemy_circle,velx,vely):
        b = 0
        c = 0 
        if enemyX < characterX and inimigoY < characterY: 
            b = enemy.move(velx,vely)
            c = enemy_circle.move(velx,vely)

        elif enemyX > characterX and inimigoY < characterY: 
            b = enemy.move(-velx,vely)
            c = enemy_circle.move(-velx,vely)

        elif enemyX < characterX and inimigoY > characterY: 
            b = enemy.move(velx,-vely)
            c = enemy_circle.move(velx,-vely)

        elif enemyX > characterX and inimigoY > characterY: 
            b = enemy.move(-velx,-vely)
            c = enemy_circle.move(-velx,-vely)

        return b , c 
    

    #posição inicial do personagem para a esfera nascer em qualquer lugar
    characterX = 100

    #contador de esferas
    contador = 0

    #chamando a função esferas para aparecer uma esfera 1 na tela
    esfera , esfera_circle = esferas(win,contador,characterX)
    


    key = win.checkKey()
    while key != "Escape":
        #velocidade do personagem
        velX = 15
        velY = 15


        #informações de cada esfera
        esfera_radius = 22    
        esferaX = esfera_circle.getCenter().getX()
        esferaY = esfera_circle.getCenter().getY()


        #informações do personagem
        character_radius = character_circle.getRadius()
        characterX = character_circle.getCenter().getX()
        characterY = character_circle.getCenter().getY()
        x_min = character.getAnchor().getX() - character.getWidth()  // 2
        y_min = character.getAnchor().getY() - character.getHeight() // 2


        #informações da imagem casa no ar
        casa_radius = casaCircle.getRadius() - 20
        casaX = casaCircle.getCenter().getX()
        casaY = casaCircle.getCenter().getY()
        

        #informações da imagem capsula
        capsule_radius = capsuleCircle.getRadius() - 20
        capsuleX = capsuleCircle.getCenter().getX()
        capsuleY = capsuleCircle.getCenter().getY()



        #a cada vez que o personagem colide com a esfera é adicionado a um contador para o programa saber a quantidade de esferas pegas
        if collided(character_radius, esfera_radius, characterX, esferaX, characterY, esferaY):
            character.move(0,0)
            character_circle.move(0,0)
            esfera_circle.move(1000,1000)
            esfera.undraw()
            contador += 1 
            esfera , esfera_circle = esferas(win,contador,characterX)



        #quando o jogador pegar um esfera spawna um inimigo que vai em direção ao personagem
        if contador >= 1:
            if freezadrawed == 0:                
                freeza.draw(win)
                freezadrawed = 1
            freezaX = freeza.getAnchor().getX()
            freezaY = freeza.getAnchor().getY()
            freezaVel , CFreezavel = enemy_follow(freeza , freezaX , freezaY , freeza_circle,0.03,0.03)
        
            #caso colida com o inimigo perde o jogo
            if collided(character_radius, freeza_radius, characterX, freezaX, characterY, freezaY) and colisao == 0:
                character_circle.move(1000,1000)
                character.move(1000,1000)
                colisao = 1
                lostImage = Image(Point(winWidth/2,winHeight/2),"youLose.png")
                lostImage.draw(win)
                message(winWidth/2, 535, "Press 'Esc' to getout",win,25,"green")



        #se o contador é maior igual a 5 aparece o terceiro inimigo na tela indo em direção do personagem
        if contador >= 3:
            if celldrawed == 0:                
                cell.draw(win)
                celldrawed = 1
            cellX = cell.getAnchor().getX()
            cellY = cell.getAnchor().getY()
            cellVel , CCellVel = enemy_follow(cell , cellX , cellY , cell_circle,0.05,0.05)

            #caso colida com o inimigo perde o jogo
            if collided(character_radius, cell_radius, characterX, cellX, characterY, cellY) and colisao == 0:
                character_circle.move(1000,1000)
                character.move(1000,1000)
                colisao = 1
                lostImage = Image(Point(winWidth/2,winHeight/2),"youLose.png")
                lostImage.draw(win)
                message(winWidth/2, 535, "Press 'Esc' to getout",win,25,"green")
                

        #se o contador é maior igual a 5 aparece o terceiro inimigo na tela indo em direção do personagem
        if contador >= 5:
            if madimbudrawed == 0:                
                madimbu.draw(win)
                madimbudrawed = 1
            madimbuX = madimbu.getAnchor().getX()
            madimbuY = madimbu.getAnchor().getY()
            madimbuVel , CMadimbuVel = enemy_follow(madimbu , madimbuX , madimbuY , madimbu_circle,0.1,0.1)

            #caso colida com o inimigo perde o jogo
            if collided(character_radius, madimbu_radius, characterX, madimbuX, characterY, madimbuY) and colisao == 0:
                character_circle.move(1000,1000)
                character.move(1000,1000)
                colisao = 1
                lostImage = Image(Point(winWidth/2,winHeight/2),"youLose.png")
                lostImage.draw(win)
                message(winWidth/2, 535, "Press 'Esc' to getout",win,25,"green")
                    


        if key == "Up":
            #teste de colisão a parte de cima da janela
            if y_min - 10<= 0:
                character.move(0,0)
                character_circle.move(0,0)

            #teste de colisão com o imagem capsula
            elif collided(character_radius, capsule_radius, characterX, capsuleX, characterY, capsuleY) and (characterY > capsuleY):
                character.move(0,0)
                character_circle.move(0,0)

            #teste de colisão com o imagem casa
            elif collided(character_radius, casa_radius, characterX, casaX, characterY, casaY) and (characterY > casaY):
                character.move(0,0)

            else:
                character.move(0,-velY)
                character_circle.move(0,-velY)



        elif key == "Down":
            #teste de colisão a parte de cima da janela
            if y_min + 115 >= winHeight:
                character.move(0,0)
                character_circle.move(0,0)

            #teste de colisão com o imagem capsula
            elif collided(character_radius, capsule_radius, characterX, capsuleX, characterY, capsuleY) and (characterY < capsuleY):
                character.move(0,0)
                character_circle.move(0,0)

            else:
                character.move(0,velY)
                character_circle.move(0,velY)



        elif key == "Left":
            #teste de colisão com a parte da esquerda da tela
            if x_min <= 0 :
                character.move(0,0)
                character_circle.move(0,0)

            #teste de colisão com o imagem capsula
            elif collided(character_radius, capsule_radius, characterX, capsuleX, characterY, capsuleY) and (characterX > capsuleX):
                character.move(0,0)
                character_circle.move(0,0)
        
            else:
                character.move(-velX,0)
                character_circle.move(-velX,0)



        if key == "Right":
            #teste de colisão com parte da direita da tela
            if x_min + 90 >= winWidth:
                character.move(0,0)
                character_circle.move(0,0)
            
            #teste de colisão com o imagem capsula
            elif collided(character_radius, capsule_radius, characterX, capsuleX, characterY, capsuleY) and (characterX < capsuleX):
                character.move(0,0)
                character_circle.move(0,0)

            #teste de colisão com o imagem casa
            elif collided(character_radius, casa_radius, characterX, casaX, characterY, casaY):
                character.move(0,0)

            else:
                character.move(velX,0)
                character_circle.move(velX,0)



        #se o contador for igual a 7, quer dizer que o personagem pegou as 7 esferas do dragão. Assim venceu o jogo
        if contador == 7:
            character.move(10000,10000)
            freeza.move(1000,1000)
            cell.move(1000,1000)
            madimbu.move(1000,1000)

            shenlong = Image(Point(winWidth/2,winHeight/2),"shenlong2.png")
            shenlong.draw(win)
            message(winWidth/2, 535, "Now you can make your desire!!", win, 25,"black")
            message(winWidth/2, 585,"Press 'Esc' to getout",win,18,"black")


        key = win.checkKey()
    
