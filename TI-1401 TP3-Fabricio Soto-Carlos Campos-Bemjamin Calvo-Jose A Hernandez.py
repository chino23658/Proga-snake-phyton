#Importamos las librerias necesarias
import pygame
from tkinter import *

#creamos variables#

#matriz=[['1', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1'], ['1', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '1'], ['1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1'], ['1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '1', '0', '0', '1'], ['1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], ['1', '1', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '1'], ['1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1'], ['1', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1'], ['1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '1', '1'], ['1', '1', '1', '0', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '1'], ['1', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '1', '1'], ['1', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '0', '1'], ['1', '1', '0', '1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1'], ['1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '1'], ['1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1'], ['1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1'], ['1', '0', '1', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1'], ['1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'], ['1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '1', '1', '1'], ['1', '0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
matriz=[['1', '2', '1', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
paredes=[]
rectangulos=[]
salidas=[]

#creamos espacio de juego

def crearmatrix(largo,ancho):
    if not isinstance(largo,int) or not isinstance(ancho,int):
        return "Error de entrada"
    else:
        cont=0
        resul=[]
        while cont!=(largo-2):
            resul+=[listfrag(["1","0"*(ancho-2),"1"])]
            cont+=1
        return[list("1"*ancho)]+ resul + [list("1"*ancho)]


def listfrag(lista):
    if not isinstance(lista,list):
        return "Error de entarada"
    else:
        resul=[]
        for ele in range(len(lista)):
            if len(lista[ele])==1:
                resul+=[lista[ele]]
            elif len(lista[ele])!=1:
                for ele1 in lista[ele]:
                    resul+=[ele1]
        return resul


#lee la matriz y crea las coordenadas de los sprites y rectangulos#

def leer(matriz):
    global rectangulos
    rectangulos=[]
    rec_pared=[]
    w=12
    h=12
    x=2
    y=2
    for vectores in matriz:
        for elemento in vectores:
            if elemento=="1" or elemento==1:
                rectangulos.append(pygame.Rect(x+2.5,y+2.5,w,h))
                rec_pared.append((x,y))
                x+=16
            if elemento=="0" or elemento==0:
                x+=16
            if elemento=="2" or elemento==2:
                x+=16
            if elemento=="3" or elemento==3:
                x+=16
        y+=16
        x=2
    return rec_pared

#busca el inicio y da las coordenadas de la misma para yoda #

def inicio(matriz):
    rec_pared=[]
    x=2
    y=2
    for vectores in matriz:
        for elemento in vectores:
            if elemento=="2" or elemento==2:
                return x+1,y
            if elemento=="0" or elemento==0:
                x+=16
            if elemento=="1" or elemento==1:
                x+=16
            if elemento=="3" or elemento==3:
                x+=16
        y+=16
        x=2
    return rec_pared

#busca los finales y sus coordenadas para la creacion de sprites y rects#

def final(matriz):
    global salidas
    salidas=[]
    rec_pared=[]
    w=12
    h=12
    x=2
    y=2
    for vectores in matriz:
        for elemento in vectores:
            if elemento=="2" or elemento==2:
                x+=16
            if elemento=="0" or elemento==0:
                x+=16
            if elemento=="1" or elemento==1:
                x+=16
            if elemento=="3" or elemento==3:
                salidas.append(pygame.Rect(x+2.5,y+2.5,w,h))
                rec_pared.append((x,y))
                x+=16
        y+=16
        x=2
    return rec_pared

#juego pygame laberinto código#

def juego():
    global matriz
    print(matriz)
    laberinto=leer(matriz)
    principio=inicio(matriz)
    salida=final(matriz)
    #iniciamos los modulos#
    pygame.init()
    #creamos ventana y fondo donde se pondran imagenes#
    superficie=pygame.display.set_mode((800,450))
    #titulo de la ventana#
    pygame.display.set_caption("Yodaberinto")
    #variable de salida#
    salir=False
    #creamos un timer#
    tiempo=pygame.time.Clock()
    #datos sobre texto y su impresion#
    letra=pygame.font.SysFont("Castellar", 25, True, True)
    texto=letra.render("PythonS",0,(150,225,250))
    #extraemos musica#
#    pygame.mixer.music.load("Weird al yankovic-Yoda with lyrics.wav")
    #extraemos imagenes#
    r2d2_final=pygame.image.load("mouse.gif").convert_alpha()
    pantano_fondo=pygame.image.load("fondo.jpg").convert_alpha()
    trooper_muro=pygame.image.load("pared.gif").convert_alpha()
    yoda_jugador=pygame.image.load("jupa.gif").convert_alpha()

    #creamos variables de movimiento#
    velocidadx=0
    velocidady=0

    #asignamos sprite de RD2D#
    r2d2=pygame.sprite.Sprite()
    r2d2.image=r2d2_final
    r2d2.rect=r2d2_final.get_rect()
    r2d2.rect.top=0
    r2d2.rect.left=0

    #asignamos sprite de fondo#
    cueva=pygame.sprite.Sprite()
    cueva.image=pantano_fondo
    cueva.rect=pantano_fondo.get_rect()
    cueva.rect.top=0
    cueva.rect.left=0

    #asignamos sprite de paredes(los troopers)#
    trooper=pygame.sprite.Sprite()
    trooper.image=trooper_muro
    trooper.rect=trooper_muro.get_rect()
    trooper.rect.top=0
    trooper.rect.left=0

    #asignamos sprite de yoda(jugador)#
    yoda=pygame.sprite.Sprite()
    yoda.image=yoda_jugador
    yoda.rect=yoda_jugador.get_rect()
    yoda.rect.top=principio[1]
    yoda.rect.left=principio[0]
    #reproducimos la musica#
#    pygame.mixer.music.play(99)
    #asignamos que debe suceder al interactuar con la ventana#
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                salir = True
                break
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if velocidady==0:
                        velocidadx=0
                        velocidady-=8
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if velocidady==0:
                        velocidadx=0
                        velocidady+=8
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if velocidadx==0:
                        velocidady=0
                        velocidadx-=8
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if velocidadx==0:
                        velocidady=0
                        velocidadx+=8
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    salir = True
                    break

        if salir:
            break
        #creamos coordenadas pasadas de personaje para usarlas en colisiones#
        anteriorx=yoda.rect.left
        anteriory=yoda.rect.top
        #determinamos el movimiento del jugador#
        yoda.rect.move_ip(velocidadx,velocidady)
        #determinamos que hacer si colisiona con una pared#
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for muros in rectangulos:
                if yoda.rect.colliderect(muros):
                    yoda.rect.left=anteriorx
                    yoda.rect.top=anteriory
        #determinamos que hace si encuentra la salida#
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for R2D2 in salidas:
                if yoda.rect.colliderect(R2D2):
                    pygame.quit()
                    salir = True
                    break
        if salir:
            break
        #utilizamos el timer para delimitar el consumo de recursos de la computadora#
        tiempo.tick(15)
        #introducimos los sprites a la ventana#
        superficie.blit(cueva.image,cueva.rect)
        superficie.blit(yoda.image,yoda.rect)
        superficie.blit(texto,(563,7))
        #determinamos los sprites y rectangulos que se deben clonar#
        for muros in rectangulos:
            pygame.draw.rect(superficie,(200,200,200),muros)
        for paredes in laberinto:
            superficie.blit(trooper.image,paredes)
        for vacios in salidas:
            pygame.draw.rect(superficie,(200,200,200),vacios)
        for yodas in salida:
            superficie.blit(r2d2.image,yodas)
        #asignamos que actualice constantemente la ventana#
        pygame.display.update()
#    ventana.mainloop()
#####################################################
##
###ventana principal#
##
##ventana = Tk()
##
##ventana.title("Menú Principal") 
##ventana.minsize(250,154) 
##ventana.maxsize(250,154)
##
###Barra de herramientas#
##
##def SobreLosAutores():
##    messagebox.showinfo("Autores","Benjamin Calvo de León\nCarné: 201235868\nJuan Fabricio Soto Mejías\nCarné: 201250955\nJose Andrés Hernández\nCarné:201235912\nCarlos Alberto Campos Fuentes\nCarné: 201250962\nTarea Programada#2\nTaller de Programación\nProfesor Andrei Fuentes")
##
##def Salir():
##    messagebox.showinfo("Hasta luego","Gracias por usar Python")
##    ventana.destroy()
##
##def TablaDePuntajes():
##    return "nada"
##
##barraherramientas = Menu(ventana)
##barraherramientas.add_command(label="Autores", command=SobreLosAutores)
##barraherramientas.add_command(label="Tabla de Puntajes", command=TablaDePuntajes)
##barraherramientas.add_command(label="Salir", command=Salir)
##ventana.config(menu=barraherramientas)
##
###canvas(para color en el fondo)#
##
##canvas = Canvas(ventana , width= 500, height = 500,bg = "Black")
##canvas.place(x=0, y=0)
##
###Marcos#
##
##marco = LabelFrame(ventana, text="Python", width = 248, height = 88)
##marco.place(x = 1.5, y = 1)
##
##marco2 = LabelFrame(ventana, text="Ancho / Alto", width = 248, height = 44)
##marco2.place(x = 1.5, y = 110)
##
##
###barra de entrada#
##
##entradas_numericas1=IntVar()
##entradas_numericas2=IntVar()
##
##barra_de_entrada_Ancho=Entry(ventana, width = 11, textvariable=entradas_numericas1)
##barra_de_entrada_Ancho.place(x=24.5,y=127.5)
##
##barra_de_entrada_Alto=Entry(ventana, width = 11, textvariable=entradas_numericas2)
##barra_de_entrada_Alto.place(x=150,y=127.5)
##
###Acciones de botones#
##
##dificultad=None
##
##def Fácil():
##    global dificultad
##    dificultad="Fácil"
##    return ini()
##
##def Normal():
##    global dificultad
##    dificultad="Normal"
##    return ini()
##
##def Difícil():
##    global dificultad
##    dificultad="Difícil"
##    return ini()
##
##def ini():
##    global matriz
##    ancho = entradas_numericas1.get()
##    alto = entradas_numericas2.get()
##    print("Ancho:",ancho," Alto:",alto)
##    matriz= crearmatrix(ancho,alto)
##    if matriz != []:
##        print("Generé una matriz de",alto,"filas por",ancho,"columnas")
##        # Agregar lo que falta para las cabecillas
##        ventana.quit()
##        juego()
##    else:
##        print("Error: las dimensiones de la matriz son no válidas. Compruebe que sean valores númericos, y que estén en el rango apropiado.")
##
##        
###Botones#
##
##botonFácil = Button(ventana, text="Fácil", command=Fácil, bg = "#EFFBFB", fg = "#0B0B3B")
##botonFácil.place(x=20,y=25)
##
##botonNormal = Button(ventana, text="Normal", command=Normal, bg = "#EFFBFB", fg = "#0B0B3B")
##botonNormal.place(x=90,y=45)
##
##botonDifícil = Button(ventana, text="Difícil", command=Difícil, bg = "#EFFBFB", fg = "#0B0B3B")
##botonDifícil.place(x=190,y=55)
##
##
###abrir ventana y mantener abierta#
##
##ventana.mainloop()
