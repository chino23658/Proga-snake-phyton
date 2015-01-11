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

largo=int(input("Favor digite el largo:"))
ancho=int(input("Favor digite ancho:"))
print(crearmatrix(largo,ancho))
