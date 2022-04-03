import os
import os.path as path
from pip._vendor.distlib.compat import raw_input

def convertPalabraOnList(thisText):
    rango = len(thisText)
    newList = []
    for x in range(rango):
        newList.append(thisText[x])
    return newList;

def buscarOnText(thisLetra,thisListOrigin):
    text = thisListOrigin.find(thisLetra)
    return text;
  

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
             
def tryParseInt(s, base=10, val=False):
    try:
        a = int(s)
        return int(s,base)
    except ValueError:
        return val 
                       
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

def ObtenerMayorCoincidencia(thisListOrigin,thisPalabra):
    rango= len(thisListOrigin) 
    text = "";
    listN = [];
    for x in range(rango):
        listN.append(buscarLetra(thisPalabra,thisListOrigin[x],x));

    return(listN)      



def convertListOnText(thisList):
    newText = ''.join(thisList)
    return newText;

def convertCadenaOnList(cadena):
    cadena_Lista = []
    for letra in cadena:
        if letra != "":
            cadena_Lista.append(letra)
            
        
    return cadena_Lista

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

    
def CreacionArchivo(thisFile):
    Existe = False
    if path.exists(thisFile):
        Existe = True
    else:  
        Existe = False
    return Existe       

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







