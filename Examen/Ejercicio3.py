


def getIndexOfList(thisList, element):
    try:
        return (thisList.index(element))
    except:
        return -1

def OBtenerLetrasUnicas(thisList):
    rango = len(thisList)
    ListUnicos = []
    for i in range(rango):
        if i == 0:
            ListUnicos.append(thisList[i])
        else:
            if getIndexOfList(ListUnicos,thisList[i]) == -1:
                 ListUnicos.append(thisList[i])
                  
    return(ListUnicos)  

def ObtenerCantidadLetras(thisList,thisListOptions):
    rango = len(thisListOptions)
    total = []
    for x in range(rango):
        total.append(thisList.count(thisListOptions[x]))   
    return total;

def convertTextOnList(thisText,separador):
    try:
        listaNueva = thisText.split(separador)
        return listaNueva;
    except:
        listaVacia =[]
        print("Ocurrió un error")
        return listaVacia; 
    
def convertCadenaOnList(cadena):
    cadena_Lista = []
    for letra in cadena:
        if letra != "":
            cadena_Lista.append(letra) 
    return cadena_Lista 

def init(Cadena):
    Text = Cadena
    Text = Text.replace(" ","")   

    ListCadena = convertCadenaOnList(Text)
    ListaUnicos = OBtenerLetrasUnicas(ListCadena) 
    ListaTotalLetras = ObtenerCantidadLetras(ListCadena,ListaUnicos)


    rango = len(ListaUnicos)
    
    for i in range(rango):
        print("Opción:",ListaUnicos[i],"Cantidad de letras:",ListaTotalLetras[i])
        

init("Hola Mundo")        