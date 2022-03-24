
def getNumMayo(x,y):
    if x > y:
        return x;
    elif x == y:
        return "Igual"
    else:
        return y;
    
    
def getFactorialNumero(x):
   return x * getFactorialNumero(x-1) if x > 1 else 1;  
        
def getSumatorioLista(listaX):
    x=0
    if listaX.length == 0:
        return 0
    else:
       x = x + getSumatorioLista(listaX[1:x-1]) 
    return x;              

def hanoi(n,po,pd,pt):
    if(n>1):
        hanoi(n-1,po,pt,pd)
    print(n,po,pd)
    if(n>1):
        hanoi(n-1,pt,pd,po)  

print(getNumMayo(2,2));  


ls = [1,2,3,4,5]
print(getFactorialNumero(6));
hanoi(3,1,3,2)