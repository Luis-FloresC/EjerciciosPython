import os
import os.path as path
from pip._vendor.distlib.compat import raw_input

'''
Escriba una función que reciba como parámetro una lista enteros positivos y retorne el
Máximo común Divisor a todos ellos.
'''
def convertTextOnList(thisText,separador):
    try:
        listaNueva = thisText.split(separador)
        return listaNueva;
    except:
        listaVacia =[]
        print("Ocurrió un error")
        return listaVacia;
    


def InvertCadena(cadena):
    return cadena[::-1]
    

def convertListOnText(thisList,separador):
    newText = separador.join(thisList)
    return newText;
 
def ExistFile(thisFile):
    Existe = False
    if path.exists(thisFile):
        Existe = True
    else:  
        Existe = False
    return Existe  
 
def Init(FileOrigin,FileDestination): 
    text = "la historia que nunca termina";
    if(ExistFile(FileOrigin) == True):
                ArchivoOrigen = open(FileOrigin,"r",encoding="utf-8")
                Frase = ArchivoOrigen.read();
                ArchivoOrigen.close();
    else:
                ArchivoOrigen = open(FileOrigin,"w",encoding="utf-8");
                ArchivoOrigen.write(text);
                ArchivoOrigen.close();
    ArchivoDestino = open(FileDestination,"w",encoding="utf-8"); 
   
    text = InvertCadena(text)
    listPalabras = convertTextOnList(text," ")
    listInversa = list(reversed(listPalabras))
    PalabraInversa = convertListOnText(listInversa," ")
    print("Palabra Inversa: ",PalabraInversa) 
    ArchivoDestino.write(PalabraInversa);
    ArchivoDestino.close()  

Init("origenTexto.txt","DestinoTexto.txt")        
    
 