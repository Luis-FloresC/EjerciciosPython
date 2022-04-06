
import os
import os.path as path
from pip._vendor.distlib.compat import raw_input

listaAbecedarioEn = [["A","B" ,"C" ,"D","E" ,"F","G" ,"H","I", "J" ,"K" ,"L","M","N"], 
["Ñ", "O" ,"P" ,"Q","R", "S", "T", "U" ,"V", "W", "X", "Y","Z","-" ]]

listaAbecedarioDesen = [["A","B" ,"C" ,"D","E" ,"F","G" ,"H","I", "J" ,"K" ,"L","M","N"], 
["Ñ", "O" ,"P" ,"Q","R", "S", "T", "U" ,"V", "W", "X", "Y","Z","-" ]]


 
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

'''
Función para encriptar una letra 
@thisLetra -> Letra que vamos a encriptar
@thisListaAbecedario -> Lista que contiene el abecedario
@indice -> posición de la letra 
'''
def getLetraDesencriptada(thisLetra, thisListaAbecedario):
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


'''
Funcion paar encriptar una palabra
@thisText -> Palabra que vamos a encriptar
@thisList -> Lista que vamos a sustituir
'''
def getPalabraEncriptada(thisText,thisList):
    rango = len(thisText)
    text = ""
    for x in range(rango):
        text += (getLetraEncriptada(thisText[x],thisList)) 
    return text    

'''
Funcion para obtener la palabra desencriptada a partir del texto encriptado por
@thisText -> Palabra que se va desencriptar 
@thisList -> Lista de origen del abecedario
'''
def getPalabraDesencriptada(thisText,thisList):
    rango = len(thisText)
    
    text = ""
    for x in range(rango):
        text += (getLetraDesencriptada(thisText[x],thisList)) 
    return text      


'''
Funcion para rotar una lista en forma circular.
@thisList -> Lista que vamos a rotar
@thisText -> palabra para saber cuantas veces vamos a rotar la lista
'''
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
    
    

'''
Funcion para verificar si el archivo existe en el directorio
@thisFile -> Nombre del archivo
'''       
def CreacionArchivo(thisFile):
    Existe = False
    if path.exists(thisFile):
        Existe = True
    else:  
        Existe = False
    return Existe  


'''
Funcion para Iniciar el Proceso de encriptación y desencriptar la frase de texto corto
@FileOrigin -> Nombre del archivo de origen
@FileDestination -> Nombre del archivo de destino
'''
def init(FileOrigin,FileDestination):
    
    textA = ""
    textA2 = ""
    texto = ""
    if(CreacionArchivo(FileOrigin) == True):
            ArchivoOrigen = open(FileOrigin,"r",encoding="utf-8")
            texto = ArchivoOrigen.read();
            ArchivoOrigen.close();
    else:
            ArchivoOrigen = open(FileOrigin,"w",encoding="utf-8");
            texto = "La casa solitaria de la montaña"
            ArchivoOrigen.write(texto);
            ArchivoOrigen.close();
            
    ArchivoDestino = open(FileDestination,"w",encoding="utf-8");   
    
    listaString = convertTextOnList(texto," ")
    rango = len(listaString)     
    for x in range(rango):
        listaAbecedarioEn[1] = rotarLista(listaAbecedarioEn[1],listaString[x])
        textA += getPalabraEncriptada(listaString[x].upper(),listaAbecedarioEn) + " "

    print(textA.capitalize())
    ArchivoDestino.write(textA.capitalize());
    ArchivoDestino.close()
    listaEncrip = convertTextOnList(textA," ")
    listaEncrip.pop()
    rango = len(listaEncrip)
    for x in range(rango):
        listaAbecedarioDesen[1] = rotarLista(listaAbecedarioDesen[1],listaEncrip[x])
        textA2 += getPalabraDesencriptada(listaEncrip[x].upper(),listaAbecedarioDesen) + " "
        
    print(textA2.capitalize())
    
 
       
        
init("Ejer2Origen.txt","Ejer2Destino.txt"); 


