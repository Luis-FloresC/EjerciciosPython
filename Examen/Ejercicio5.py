
def getIndexOfList(thisList, element):
    try:
        return (thisList.index(element))
    except:
        return -1

def OBtenerVotosUnicos(thisList):
    rango = len(thisList)
    ListVotosUnicos = []
    for i in range(rango):
        if i == 0:
            ListVotosUnicos.append(thisList[i])
        else:
            if getIndexOfList(ListVotosUnicos,thisList[i]) == -1:
                 ListVotosUnicos.append(thisList[i])
                  
    return(ListVotosUnicos)            
              
        
def ObtenerCantidadVotos(thisListVotos,thisListOptions):
    rango = len(thisListOptions)
    totalVotos = []
    for x in range(rango):
        totalVotos.append(thisListVotos.count(thisListOptions[x]))   
    return totalVotos;            

ListaVotos = ["A","A","A","A","A","A","A","A","A","B","A","B","C","A","D","H","B","A","C","B","A","D","D","D","A","B","C"]
ListaVotosUnicos = OBtenerVotosUnicos(ListaVotos) 
ListaTotalVotos = ObtenerCantidadVotos(ListaVotos,ListaVotosUnicos)

rango = len(ListaVotosUnicos)
print("Total de Votos")
for i in range(rango):
    print("Opción:",ListaVotosUnicos[i],"Cantidad de Votos:",ListaTotalVotos[i])
    
 
TotalVotos = len(ListaVotos)
print("Total Votos",TotalVotos)     

if((TotalVotos/ 2) < ListaTotalVotos[0]):
    print("Obtiene la mayoria absoluta de votos")