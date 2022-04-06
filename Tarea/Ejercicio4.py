
import os
import os.path as path
from pip._vendor.distlib.compat import raw_input
from math import ceil

'''
Funcion para encriptar un texto largo.
@thisText -> Texto que vamos a encriptar
'''
def GetPalabraEncriptada(thisText):
    try:    
        textEncriptado = ""
        allmatriz = Matriz5x25(thisText)
        for matriz in allmatriz:
            resultMatriz = TransponerMatriz(matriz)
            for i in range(5):
                for j in range(25):
                    textEncriptado += resultMatriz[i][j]
        return textEncriptado
    except: 
        return("Ocurrió un error")
        
'''
Funcion para convertir el texto de origen en una matriz  de 5 filas por 25 columnas.
@thisFrase -> Frase que vamos a convertir en matriz
'''
def Matriz5x25(thisFrase):
        allMatriz = []
        totalLetras = len(thisFrase)
        totalIteraciones = ceil(totalLetras / 125)
        for h in range(0, totalIteraciones):
            matriz = []
            for i in range(5):
                matriz.append([])
                for j in range(25):
                    if totalLetras > 0:
                        if(i==0):
                            matriz[i].append(thisFrase[j])
                        else:
                            matriz[i].append(thisFrase[j+25*i])

                        totalLetras -= 1
                            
                    else:
                        matriz[i].append(" ")
            allMatriz.append(matriz)
        return allMatriz
    
'''
Funcion para Obtener el texto largo desencriptados
@thisText -> texto encriptado
'''
def GetPalabraDesencriptada(thisText):
    textDesencriptado = ""
    allmatriz= Matriz5x25(thisText)
    for matriz in allmatriz:
        resultMatriz = TransponerMatriz(matriz)
        for i in range(5):
            for j in range(25):
                textDesencriptado += resultMatriz[i][j]
    return textDesencriptado
    

'''
Funcion para transponer una matriz
@thisMatriz -> Matriz que vamos a transponer
'''    
def TransponerMatriz(thisMatriz):
        resultMatriz = []
        matriz_5x5 = []
        allMatriz_5x5 = []
        for h in range(0, 5):
            # matriz_5x5.append([])
            for i in range(5):
                matriz_5x5.append([])
                for j in range(5):
                    matriz_5x5[i].append(thisMatriz[i][j+(h*5)])
            allMatriz_5x5.append(matriz_5x5)
            matriz_5x5 = []
        # filas por columnas
        for i in range(5):
            resultMatriz.append([])
            for fila in allMatriz_5x5:
                for j in range(5):
                    resultMatriz[i].append(fila[j][i])

        
        return resultMatriz    

'''
Funcion para verificar si el archivo existe en el directorio
@thisFile -> Nombre del archivo
'''
def ExistFile(thisFile):
    Existe = False
    if path.exists(thisFile):
        Existe = True
    else:  
        Existe = False
    return Existe  
    

'''
Funcion para Iniciar el Proceso de encriptacion y desencriptar la frase de texto largo
@FileOrigin -> Nombre del archivo de origen
@FileDestination -> Nombre del archivo de destino
'''    
def Init(FileOrigin,FileDestination):
    try:
        Frase = '''El término "big data" se  refiere a los datos que son tan grandes, rápidos o complejos que es difícil procesarlos'''
        textEncriptado = ""
        if(ExistFile(FileOrigin) == True):
                ArchivoOrigen = open(FileOrigin,"r",encoding="utf-8")
                Frase = ArchivoOrigen.read();
                ArchivoOrigen.close();
        else:
                ArchivoOrigen = open(FileOrigin,"w",encoding="utf-8");
                ArchivoOrigen.write(Frase);
                ArchivoOrigen.close();
        ArchivoDestino = open(FileDestination,"w",encoding="utf-8"); 
        textEncriptado = GetPalabraEncriptada(Frase);
        print("Texto Encriptado:",textEncriptado);   
        print("Texto Desencriptado: ",GetPalabraDesencriptada(textEncriptado))
        ArchivoDestino.write(textEncriptado);
        ArchivoDestino.close()           
                
    except:
        print("Ocurrió un Error")        


Init("Ejer4Origen.txt","Ejer4Destino.txt");