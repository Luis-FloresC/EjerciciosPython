
 
'''
Función para obtener el indice de un elemento en la lista
@thisList -> Lista donde se realiza la buscaqueda de indice por elemento
@element -> ELemento que se busca en la lista
'''
def getIndexOfList(thisList, element):
    try:
        return (thisList.index(element))
    except:
        return -1

'''
Funcion para convertir una cadena de texto en una lista de
@thisText -> cadena de texto que vamos a convertir un
@separador -> el separador por el cual vamos a dividir la cadena en partes
'''
def convertTextOnList(thisText,separador):
    try:
        listaNueva = thisText.split(separador)
        return listaNueva;
    except:
        listaVacia =[]
        print("Ocurrió un error")
        return listaVacia;

'''
Función para encriptar una letra 
@thisLetra -> Letra que vamos a encriptar
@thisListaAbecedario -> Lista que contiene el abecedario
@indice -> posición de la letra 
'''
def getLetraEncriptada(thisLetra, thisListaAbecedario):
    try:
        index = getIndexOfList(thisListaAbecedario[0], thisLetra)
        
        if(index == -1):
            index = getIndexOfList(thisListaAbecedario[1], thisLetra)
            thisLetra = thisListaAbecedario[0][index]
        else:
             thisLetra = thisListaAbecedario[1][index]   
        
        return thisLetra
    except:
        return("Ocurrió un error")

def getPalabraEncriptada(thisText,thisList):
    rango = len(thisText)
    text = ""
    for x in range(rango):
        text += (getLetraEncriptada(thisText[x],thisList)) 
    return text    
    

def rotarLista(thisList,thisText):
    try:
        rango = len(thisText)
        for x in range(rango):
            thisList.insert(0,thisList.pop())
             
        return thisList
    except:
        listaVacia =[]
        print("Ocurrió un error")
        return listaVacia;
    


ls = [["A","B" ,"C" ,"D","E" ,"F","G" ,"H","I", "J" ,"K" ,"L","M","N"], 
["Ñ", "O" ,"P" ,"Q","R", "S", "T", "U" ,"V", "W", "X", "Y","Z","-" ]]


def init():
    texto = "La Casa Solitaria de la montaña en new york"
    listaString = convertTextOnList(texto," ")
    rango = len(listaString)
    textA = ""
    for x in range(rango):
        ls[1] = rotarLista(ls[1],listaString[x])
        textA += getPalabraEncriptada(listaString[x].upper(),ls) + " "

    print(textA)
        
init();


