
from tkinter import *

out = open("puntaje.txt","w")
out.write("Fabricio,20    \n")
out.write("Carlos,20     \n ")
out.write("Chino,20      \n  ")
out.write("Ben,20        \n ")
out.write("Fabricio,20    \n")
out.write("Carlos,20     \n ")
out.write("Chino,20      \n  ")
out.write("Ben,20         ")
out.close()

def puntaje(score):
    leer= open(score,"r")
    lista=leer.readlines()

    nuevo=""
    for e in lista:
        nuevo+=e
    return nuevo
   
score="puntaje.txt"

ventana= Tk()
ventana.title("Puntajes")
frame=Frame(height=200, width= 300,bg="white")
frame.pack()

#*********************
def ocultar():
    ventana.withdraw()
#************************5******ocultar***********

canvas = Canvas(ventana , width= 300, height = 200, bg = "red")
canvas.create_text(40,10,text=puntaje(score), font = ("Dungeon","12"),anchor =NW)
Boton19=Button(ventana,text="Ocultar", width=7,height=3, command=ocultar,bg="black",fg="white")
Boton19.place(x=235,y=140)

#*****************************************************************************************

canvas.place(x=-1, y=-1)
ventana.mainloop()



