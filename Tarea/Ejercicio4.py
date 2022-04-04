
import os
import os.path as path
from pip._vendor.distlib.compat import raw_input
from math import ceil

def GetPalabraEncriptada(thisText):
    try:    
        encrypt_message = ""
        allmatriz= matriz_5x25(thisText)
        for matriz in allmatriz:
            transp_matriz = transponer_matriz(matriz)
            for i in range(5):
                for j in range(25):
                    encrypt_message += transp_matriz[i][j]
        return encrypt_message
    except: 
        return("Ocurrió un error")
        

def matriz_5x25(pharse):
        allMatriz = []
        coun_letters = len(pharse)
        count_laps = ceil(coun_letters / 125)
        for h in range(0, count_laps):
            matriz = []
            for i in range(5):
                matriz.append([])
                for j in range(25):
                    if coun_letters > 0:
                        if(i==0):
                            matriz[i].append(pharse[j])
                        else:
                            matriz[i].append(pharse[j+25*i])

                        coun_letters -= 1
                            
                    else:
                        matriz[i].append(" ")
            allMatriz.append(matriz)
        return allMatriz

def decrypt(thisText):
    decrypt_message = ""
    allmatriz= matriz_5x25(thisText)
    for matriz in allmatriz:
        transp_matriz = transponer_matriz(matriz)
        for i in range(5):
            for j in range(25):
                decrypt_message += transp_matriz[i][j]
    return decrypt_message
    
def transponer_matriz(matriz):
        transp_matriz = []
        matriz_5x5 = []
        allMatriz_5x5 = []
        for h in range(0, 5):
            # matriz_5x5.append([])
            for i in range(5):
                matriz_5x5.append([])
                for j in range(5):
                    matriz_5x5[i].append(matriz[i][j+(h*5)])
            allMatriz_5x5.append(matriz_5x5)
            matriz_5x5 = []


        # filas por columnas
        for i in range(5):
            transp_matriz.append([])
            for fila in allMatriz_5x5:
                for j in range(5):
                    transp_matriz[i].append(fila[j][i])

        
        return transp_matriz    


def CreacionArchivo(thisFile):
    Existe = False
    if path.exists(thisFile):
        Existe = True
    else:  
        Existe = False
    return Existe  
    
    
def Init(FileOrigin,FileDestination):
    try:
        Frase = '''
                El término "big data" se  refiere a los datos que son tan grandes, rápidos o complejos que es difícil procesarlos
                '''
        textEncriptado = ""
        if(CreacionArchivo(FileOrigin) == True):
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
        print("Texto Desencriptado: ",decrypt(textEncriptado))
        ArchivoDestino.write(textEncriptado);
        ArchivoDestino.close()           
                
    except:
        print("Ocurrió un Error")        


Init("Ejer4Origen.txt","Ejer4Destino.txt");