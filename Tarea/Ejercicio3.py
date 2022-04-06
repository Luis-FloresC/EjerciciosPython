import os
import os.path as path
from pip._vendor.distlib.compat import raw_input

'''
Funcion para convertir una palabra en una lista.
@thisText -> palabra que vamos a separar letra por letra
'''
def convertPalabraOnList(thisText):
    rango = len(thisText)
    newList = []
    for x in range(rango):
        newList.append(thisText[x])
    return newList;

'''
Funcion para buscar una letra en un texto
@thisLetra -> Letra que estamos buscando
@thisListOrigin -> Lista donde vamos a buscar la letra
'''
def buscarOnText(thisLetra,thisListOrigin):
    text = thisListOrigin.find(thisLetra)
    return text;
  
'''
Funcion para obtener el elemeto de una lista por medio de su index.
@thisList -> Lista donde buscaremos el valor.
@index -> posición que vamos a buscar el elemento
'''
def getValorOfList(thisList, index): 
    try:
      # newlist = convertCadenaOnList(thisList)
       index = int(index)
       letra = thisList[index]
       return (letra)
    except:
        return -1;   
        
  

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
Funcion que los devuelve una lista con el mayor coincidencas en la palabra.
@thisList -> Lista donde vamos  buscar la palabra 
'''    
def MayorNumeroPalabras(thisList):
    
    rango = len(thisList)
    newList = []
    for x in range(rango):
        newList.append(converListonEntero(thisList[x]))
    mayor = 0
    valor = 0;
    
    rango = len(newList)
    for x in range(rango):
        if mayor < len(newList[x]):
            valor = x
            mayor = len(newList[x])
    return valor      

'''
Funcion para Comprobar si un numero es entero
@isNum -> dato que vamos a validar si es numero

'''             
def tryParseInt(isNum, base=10, val=False):
    try:
        a = int(isNum)
        return int(isNum,base)
    except ValueError:
        return val 

'''
Funcion para convertir todos los valores de la lista solo en números enteros
@thisList -> Lista que vamos a convertir
'''                       
def converListonEntero(thisList):
    newList = []
    thisText = convertListOnText(thisList)
    #print(thisText)
    rango = len(thisText)
    for x in range(rango):
        if(tryParseInt(thisList[x])):
            newList.append(thisList[x])
        #newList.append(thisList[x])
    return newList    
    
'''
Funcion para buscar una letra en la lista de 10 palabras de origen
@thisPalabra -> palabra que vamos a buscar coincidencas
@thisList -> Lista donde vamos a buscar que coincida esa palabra
@num -> posición de la palabra donde vamos a buscar coincidencas
'''
def buscarLetra(thisPalabra,thisList,num):
    listNew = convertPalabraOnList(thisPalabra)
    rango = len(listNew)
    cont = 0
    text = ""
    listCoincidencia = []
    
    for x in range(rango):
        if(buscarOnText(listNew[x],thisList) != -1): 
            if(x == 0):
                listCoincidencia.append((str)(num))
            listCoincidencia.append((str)(buscarOnText(listNew[x],thisList)))
        else:
            if(x == 0):
                listCoincidencia.append((str)(num))
            listCoincidencia.append((str)(listNew[x]))
            text += "-"    
         
    return listCoincidencia   

'''
Funcion para obtener la lista de coincidencias por cada una de las 10 palabras.
@thisListOrigin -> Lista donde vamos a buscar la coincidencias.
@thisPalabra -> Palabra donde vamos a buscar el mayor número de coincidencias
'''
def ObtenerMayorCoincidencia(thisListOrigin,thisPalabra):
    rango= len(thisListOrigin) 
    text = "";
    listN = [];
    for x in range(rango):
        listN.append(buscarLetra(thisPalabra,thisListOrigin[x],x));

    return(listN)      


'''
Funcion para unir una lista en una palabra.
@thisList -> Lista que vamos a unir en una palabra
'''
def convertListOnText(thisList):
    newText = ''.join(thisList)
    return newText;

'''
Funcion para convertir una Cadena de texto en Lista.
@cadena ->  Cadena de texto
'''
def convertCadenaOnList(cadena):
    cadena_Lista = []
    for letra in cadena:
        if letra != "":
            cadena_Lista.append(letra) 
    return cadena_Lista
'''
Funcion para desencriptar la palabra encriptada
@thisList -> Lista de palabras donde vamos a buscar
@thisPalabra ->Palabra encriptada que vamos a desencriptar
'''
def desencriptarPalabra(thisList,thisPalabra):
    listTemporal = convertCadenaOnList(thisPalabra);
    index = int(listTemporal[0]);  
    listTemporal.pop(0);
    thisPalabra = convertListOnText(listTemporal)
    rango = len(thisPalabra)
    text = ""
    for i in range(rango):
        if (getValorOfList(thisList[index],thisPalabra[i])!= -1):
            text  += getValorOfList(thisList[index],thisPalabra[i])       
        else:
            text += thisPalabra[i]
    return text

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
Funcion para Iniciar el Proceso de encriptación y desencriptar la frase de texto largo
@FileOrigin -> Nombre del archivo de origen
@FileDestination -> Nombre del archivo de destino
'''
def init(FileOrigin,FileDestination):
    Palabra = "La Casa Solitaria de la Montaña de Luis"
    if(CreacionArchivo(FileOrigin) == True):
            ArchivoOrigen = open(FileOrigin,"r",encoding="utf-8")
            Palabra = ArchivoOrigen.read();
            ArchivoOrigen.close();
    else:
            ArchivoOrigen = open(FileOrigin,"w",encoding="utf-8");
            Palabra = "La casa solitaria de la montaña"
            ArchivoOrigen.write(Palabra);
            ArchivoOrigen.close();
            
    ArchivoDestino = open(FileDestination,"w",encoding="utf-8");
    listPalabras = [
        "MURCIELAGO",
        "HIPOTENUSA",
        "ESCUPITAJO",
        "SUDORIENTA",
        "DESAHUCIOS",
        "SUPONIERAN",
        "ARQUITECTO",
        "CEDULACIÓN",
        "CUESTIONAR",
        "ESQUILADOR"]
    
    listPalabrasText = convertTextOnList(Palabra," ")
    rango = len(listPalabrasText)
    text = ""
    for x in range(rango):
        listasR = ObtenerMayorCoincidencia(listPalabras,listPalabrasText[x].upper())
        indiceMax = MayorNumeroPalabras(listasR)
        text += convertListOnText(listasR[indiceMax]) + " "
    print("Texto Encriptado:",text)
    ArchivoDestino.write(text.capitalize());
    ArchivoDestino.close()
    listEncriptada = convertTextOnList(text," ")
    listEncriptada.pop()
    rango = len(listEncriptada)
    
    text2 = ""
    for x in range(rango):
        text2 += desencriptarPalabra(listPalabras,listEncriptada[x]) + " "
    print("Texto Desencriptado:" ,text2.capitalize())
    
init("Ejer3Origen.txt","Ejer3Destino.txt");







