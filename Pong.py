import tkinter
from tkinter import *
import pygame
import time
import sys
import os

def juego():
    #Inicializar pygame
    pygame.init()

    #Colores
    purple=(204,153,255)
    black=(0,0,0)
    

    #Pantalla
    ancho_pantalla = 600
    alto_pantalla = 400
    pantalla = pygame.display.set_mode((ancho_pantalla,alto_pantalla))
    pygame.display.set_caption('Pong')
    font = pygame.font.SysFont('Nirmala UI',40)

    #Pelota
    pelotax = int(ancho_pantalla / 2)
    pelotay = int(alto_pantalla / 2)
    pelotaxv = 4
    pelotayv = 4
    pelotar = 10

    #Raqueta 1 y 2
    raquetax1 = 5
    raquetay1 = 10
    raqueta_ancho1 = 15
    raqueta_alto1 = 110

    raquetax2 = ancho_pantalla-21
    raquetay2 = 10
    raqueta_ancho2 = 15
    raqueta_alto2 = 110

    #Puntaje de los jugadores
    puntuj1 = 0
    puntuj2 = 0
    pygame.mouse.set_visible(0)
    puntaje_Fuente = pygame.font.Font(None,25)
    puntaje_Texto = puntaje_Fuente.render("Score",0,(204,153,255))

    do_main=True
    subioV = False
    PuntajeF = False

    #Teclado
    while do_main:
        pressed=pygame.key.get_pressed()
        pygame.key.set_repeat()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_main=False
        if pressed[pygame.K_ESCAPE]:
            do_main=False
        if pressed[pygame.K_w]:
            raquetay1-=5
        elif pressed[pygame.K_s]:
            raquetay1+=5

        if pressed[pygame.K_UP]:
            raquetay2-=5
        elif pressed[pygame.K_DOWN]:
            raquetay2+=5

        pelotax+=pelotaxv
        pelotay+=pelotayv

        #colisión de la bola arriba abajo
        if pelotay -pelotar <= 0 or pelotay + pelotar >= alto_pantalla:
            pelotayv*=-1

        #Collision de las raquetas arriba abajo
            if raquetay1 < 0:
                raquetay1 = 0
            elif raquetay1 + raqueta_alto1 > alto_pantalla:
                raquetay1= alto_pantalla - raqueta_alto1

            if raquetay2<0:
                raquetay2=0
            elif raquetay2 + raqueta_alto2 > alto_pantalla:
                raquetay2 = alto_pantalla - raqueta_alto2

        #Golpe de pelota con raquetas
        if pelotax < raquetax1 + raqueta_ancho1 and pelotay >= raquetay1 and pelotay <= raquetay1 + raqueta_alto1:
            pelotaxv*=-1
        if pelotax> raquetax2 and pelotay >= raquetay2 and pelotay <= raquetay2 + raqueta_alto2:
            pelotaxv*=-1

        #Puntaje
        if pelotax <= 0:
            puntuj2+=1
            pelotax = int(alto_pantalla / 2)
            pelotay = int(ancho_pantalla / 2)
        if pelotax >= ancho_pantalla:
            puntuj1+=1
            pelotax = int(alto_pantalla / 2)
            pelotay = int(ancho_pantalla / 2)

        #Pantalla del juego
        pantalla.fill(black)
        raqueta1=pygame.draw.rect(pantalla,purple,(raquetax1,raquetay1,raqueta_ancho1,raqueta_alto1),0)
        raqueta2=pygame.draw.rect(pantalla,purple,(raquetax2,raquetay2,raqueta_ancho2,raqueta_alto2),0)
        net=pygame.draw.line(pantalla,purple,(300,20),(300,400))
        pelota=pygame.draw.circle(pantalla,purple,(pelotax,pelotay),pelotar,0)
        textopuntaje=font.render(str(puntuj1)+"  "+str(puntuj2),1,purple)
        pantalla.blit(textopuntaje,(ancho_pantalla/2-textopuntaje.get_width()/2,10))
        pantalla.blit(puntaje_Texto,(277,3))

        pygame.display.update()
        time.sleep(0.01666667)

        #Puntaje final
        if puntuj1 == 20 or puntuj2 == 20:
            print("\n--------------------GAME OVER--------------------\n")
            print("Puntaje jugador 1:",puntuj1)
            print("Puntaje jugador 2:",puntuj2)
            sys.exit()

    pygame.quit()


#Funcion archivo como jugar
def archivo():
    archivo = os.popen('Como jugar.pdf')
    print(archivo)

#Pantalla de inicio
ventana_inicio = Tk()
ventana_inicio.geometry("600x400")
ventana_inicio.config(bg = "black")
imagen = tkinter.PhotoImage(file = "pong.png")
ImagenEnPantalla = tkinter.Label(ventana_inicio, image = imagen).place(x=170,y=50)
botonJugar = Button(ventana_inicio,text = "Jugar",command = juego)
botonCJugar = Button(ventana_inicio,text = "Como jugar", command = archivo)
botonJugar.place(x=290,y=300)
botonCJugar.place(x=270,y=330)
ventana_inicio.mainloop()

