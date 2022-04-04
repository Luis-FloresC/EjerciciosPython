import os
import os.path as path
from pip._vendor.distlib.compat import raw_input

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
        listaAbecedario = [ "A", "B", "C", "D", "E", 
                            "F", "G", "H", "I", "J", 
                            "K","L", "M", "N", "Ñ", 
                            "O", "P", "Q", "R", "S", 
                            "T", "U", "V", "W", "X", 
                            "Y", "Z"]
        rango = len(thisTexto)
        for x in range(rango):
            text += (getLetraEncriptada(thisTexto[x], listaAbecedario, x+1))
        return (text)
    except:
        return("Ocurrió un error")

'''
Función para desencriptar texto  
@thisTexto -> Palabra que vamos a desencriptar
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


'''
Funcion para validar los número que se encuentre en un rango
@numero -> número que vamos a evaluar
@rangoMinimo -> Rango mínimo que puede se puede permitir 
@rangoMaximo -> Rango máximo que puede se puede permitir 
'''
def validarNumeros(numero,rangoMinimo,rangoMaximo):
    if numero < rangoMinimo or numero > rangoMaximo:
        return numero - rangoMaximo - 1
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
      #  print("Index",(getIndexOfList(thisListaAbecedario, thisLetra)),"indice",indice)
        index = (getIndexOfList(thisListaAbecedario, thisLetra)-indice )
        thisLetra = thisListaAbecedario[(index)]
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
            index = (validarNumeros(index,0,26))
  
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
 
 

def CreacionArchivo(thisFile):
    Existe = False
    if path.exists(thisFile):
        Existe = True
    else:  
        Existe = False
    return Existe   
            
#Funcion para iniciar el proceso de encriptación
def init(FileOrigin,FileDestination):
    try:
        text = ""
        textDesencriptado = ""
      # ArchivoOrigen = open(FileOrigin,"r")
        textoEncriptar="";
        if(CreacionArchivo(FileOrigin) == True):
            ArchivoOrigen = open(FileOrigin,"r",encoding="utf-8")
            textoEncriptar = ArchivoOrigen.read();
            ArchivoOrigen.close();
        else:
            ArchivoOrigen = open(FileOrigin,"w",encoding="utf-8");
            textoEncriptar = "La casa solitaria de la montaña"
            ArchivoOrigen.write(textoEncriptar);
            ArchivoOrigen.close();
            
        
        ArchivoDestino = open(FileDestination,"w",encoding="utf-8");
          
        
        
        listaStr = convertTextOnList(textoEncriptar," ");
        rango = len(listaStr)     
        for x in range(rango):
            text += (getPalabraEncriptada(listaStr[x].upper())) + " "
        
        listEncriptada = convertTextOnList(text," ")
        rango = len(listEncriptada)
        
        for x in range(rango):
            textDesencriptado += (getPalabraDesencriptada((listEncriptada[x].upper()))) + " " 
        
        ArchivoDestino.write(text.capitalize());
        ArchivoDestino.close()
        print("Texto Encriptado: ",text.capitalize())    
        print("Texto Desencriptado: ", textDesencriptado.capitalize())         
    except:
        print("Ocurrió un error")
    
init("Ejer1Origen.txt","Ejer1Destino.txt");    


