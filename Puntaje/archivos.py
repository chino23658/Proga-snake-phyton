out = open("puntaje.txt","w")
out.write("Fabricio,20\n")
out.write("Carlos,20\n")
out.write("Chino,20\n")
out.write("Ben,20\n")
out.close()

def puntaje(score):
    leer= open(score,"r")
    lista=leer.readlines()
    
    for l in lista:
        if l== "\n":
            l.split(",")
        print(l)
    
   
score=puntaje("puntaje.txt")





