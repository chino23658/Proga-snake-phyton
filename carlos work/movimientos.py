matriz=[[0,0 ], [0, 16], [0, 32]]
def abajo(matriz):#abajo#
    ultimo=[]
    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][0]+16]
    ultimo+=[matriz[-1][1]]
    matriz.append(ultimo)
    return matriz

    
def derecha(matriz):#derecha#
    ultimo=[]
    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][0]]
    ultimo+=[matriz[-1][1]+16]
    matriz.append(ultimo)
    return matriz
    
def izquierda(matriz):#izquierda#
    ultimo=[]
    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][0]]
    ultimo+=[matriz[-1][1]-16]
    matriz.append(ultimo)
    return matriz
   
def arriba(matriz):#arriba#
    ultimo=[]
    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][1]-16]
    ultimo+=[matriz[-1][0]]
    matriz.append(ultimo)
    return matriz


def abajo_agregado(matriz):#ab#
    ultimo=[]
##    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][0]+16]
    ultimo+=[matriz[-1][1]]
    matriz.append(ultimo)
    return matriz

    
def derecha_agregado(matriz):#der#
    ultimo=[]
##    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][0]]
    ultimo+=[matriz[-1][1]+16]
    matriz.append(ultimo)
    return matriz
    
def izquierda_agregado(matriz):#izq#
    ultimo=[]
##    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][0]]
    ultimo+=[matriz[-1][1]-16]
    matriz.append(ultimo)
    return matriz
   
def arriba_agregado(matriz):#arr#
    ultimo=[]
##    matriz.remove(matriz[0])
    ultimo+=[matriz[-1][1]-16]
    ultimo+=[matriz[-1][0]]
    matriz.append(ultimo)
    return matriz
