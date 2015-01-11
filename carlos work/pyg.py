import pygame
def main():
    pygame.init()#invocacion de modulos
    pantalla=pygame.display.set_mode([300,300])#pantalla principal
    salir=False#bandera
    reloj=pygame.time.Clock()#variables
    #colores
    blanco=(255,255,255)
    rojizo=(200,20,50)
    azulado=(70,70,190)
    #rectangulos
    rec=pygame.Rect(50,50,45,45)
    rec2=pygame.Rect(200,200,100,50)

    #ventana
    s=pygame.Surface((100,100))#ventanas tamano
    s.fill(rojizo)#pintar ventana

    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
                #movimiento de acuerdo a lo seleccionado
            if event.type==pygame.MOUSEBUTTONDOWN:
                rec=rec.move(10,10)#rec.move_ip(10,10) es un disminutivo

                
                #se ubican en la superficie
        reloj.tick(20)#tiempo de actualiza para reducir el proceso de funcionamiento
        pantalla.fill(blanco)
        pantalla.blit(s,[100,100],)#imprime y ubica el canvas
        #impresion rectangulos
        pygame.draw.rect(pantalla,rojizo,rec)
        pygame.draw.rect(pantalla,azulado,rec2)

        
        pygame.display.update()
    pygame.quit()
main()
