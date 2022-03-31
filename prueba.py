
ls = [["A","B" ,"C" ,"D","E" ,"F","G" ,"H","I", "J" ,"K" ,"L","M","N"], 
["Ñ", "O" ,"P" ,"Q","R", "S", "T", "U" ,"V", "W", "X", "Y","Z","-" ]]

ls2 = [["A","B" ,"C" ,"D","E" ,"F","G" ,"H","I", "J" ,"K" ,"L","M","N"], 
["Ñ", "O" ,"P" ,"Q","R", "S", "T", "U" ,"V", "W", "X", "Y","Z","-" ]]


def rotarLista(thisList,thisText,isInverse):
    try:
        if not isInverse:
            rango = len(thisText)
            for x in range(rango):
                thisList.insert(0,thisList.pop())
        else:
            rango = len(thisText)
            for x in range(rango):
                thisList.insert(13,thisList.pop(0))    
        return thisList
    except:
        listaVacia =[]
        print("Ocurrió un error")
        return listaVacia;
    

print("Normal\n",ls[0])
print(ls[1],"\n")


ls[1] = rotarLista(ls[1],"LA",False)    
print(ls[0])
print(ls[1],"\n")

ls[1] = rotarLista(ls[1],"CASA",False)    
print(ls[0])
print(ls[1],"\n")


ls2[0] = rotarLista(ls2[0],"CASA",True)  
ls2[1] = rotarLista(ls2[1],"CASA",True)    
print(ls[0])
print(ls[1],"\n")

ls2[0] = rotarLista(ls2[0],"LA",True)  
ls2[1] = rotarLista(ls2[1],"LA",True)    
print(ls[0])
print(ls[1],"\n")


