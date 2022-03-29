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
Función para encriptar texto  
@thisTexto -> Palabra que vamos a encriptar
'''
def getPalabraEncriptada(thisTexto):
    try:
        text = ""
        listaAbecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                           "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        rango = len(thisTexto)
        for x in range(rango):
            text += (getLetraEncriptada(thisTexto[x], listaAbecedario, x+1))
        return (text)
    except:
        return("Ocurrió un error")

'''
Función para encriptar texto  
@thisTexto -> Palabra que vamos a encriptar
'''
def getPalabraDesencriptada(thisTexto):
    try:
        text = ""
        listaAbecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                           "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        rango = len(thisTexto)
        for x in range(rango):
            text += (getLetraDesencriptada(thisTexto[x], listaAbecedario, x+1))
        return (text)
    except:
        return("Ocurrió un error")



def validarNumeros(numero,rangoMinimo,rangoMaximo):
    if numero < rangoMinimo or numero > rangoMaximo:
        return 0
    else:
        return numero
    


'''
Función para desencriptar una letra 
@thisLetra -> Letra que vamos a encriptar
@thisListaAbecedario -> Lista que contiene el abecedario
@indice -> posición de la letra 
'''
def getLetraDesencriptada(thisLetra, thisListaAbecedario, indice):
    try:
        index = getIndexOfList(thisListaAbecedario, thisLetra) - indice

            
  
        thisLetra = thisListaAbecedario[index]
        return thisLetra
    except:
        return("Ocurrió un error")


'''
Función para encriptar una letra 
@thisLetra -> Letra que vamos a encriptar
@thisListaAbecedario -> Lista que contiene el abecedario
@indice -> posición de la letra 
'''
def getLetraEncriptada(thisLetra, thisListaAbecedario, indice):
    try:
        index = getIndexOfList(thisListaAbecedario, thisLetra)  + indice
        if index > 26:
            index = validarNumeros(index,1,26) + indice
  
        thisLetra = thisListaAbecedario[index]
        return thisLetra
    except:
        return("Ocurrió un error")

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
            

#Funcion para iniciar el proceso de encriptación
def init():
    try:
        text = ""
        textDesencriptado = ""
        
        textoEncriptar = input("Ingrese cadena de Texto: ")
        listaStr = convertTextOnList(textoEncriptar," ");

        rango = len(listaStr)
        
        for x in range(rango):
            text += (getPalabraEncriptada(listaStr[x].upper())) + " "
        
        listEncriptada = convertTextOnList(text," ")
        rango = len(listEncriptada)
        
        for x in range(rango):
            textDesencriptado += (getPalabraDesencriptada(listEncriptada[x].upper())) + " " 
        
        print("Texto Encriptado: ",text.capitalize())    
        print("Texto Desencriptado: ", textDesencriptado.capitalize())         
    except:
        print("Ocurrió un error")
    
init()    


