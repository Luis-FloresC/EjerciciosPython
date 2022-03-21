x = int(input("Ingrese un Numero 1: "))
y = int(input("Ingrese un Numero 1: "))
myList = []
menu = "1. {0}\n2. {1}\n3. {2}\n4. {3}"
print(menu.format("Suma","Resta","Multiplicación","Dividir"))
op = int(input("Seleccione la operacion: "))


while(op <= 0 or op >= 3):
    print("Opción no Valida!")
    print(menu.format("Suma","Resta","Multiplicación","Dividir"))
    op = int(input("Seleccione la operacion: "))
    

if op == 1:
    print("La suma es: ",x+y)
    myList.append(x+y)
elif op == 2:
    myList.append(x-y)
    print("La resta es: ",x-y)  
elif op == 3:
    print("La multiplicación es: ",x*y)
    myList.append(x*y)
else:
    if y == 0:
        print("No se puede dividir por cero")
        myList.append("Error")
    else:
        print("La división es: ",x/y)
        myList.append(x/y)
            
     

ListN = [7,2,7,2,4]
  
ListN.pop(0)  
print(ListN)
  
                  