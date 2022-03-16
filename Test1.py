
from operator import xor
from pickle import TRUE


try:
    print("Hola Mundo")
    dato = input("Ingrese un Valor: ")

    for i in range(int(dato)):
        print(i)

    print(type(dato))
    potencia = "La potencia de {0} es: {1}"
    sumaComplex = "( {0} + {1} ) = {2}"
    MultoComplex = "( {0} * {1} ) = {2}"
    a = 4j + int(dato)
    b = 2j + int(dato)
    print(sumaComplex.format(a,b,a+b))
    print(MultoComplex.format(a,b,a*b))
    print(xor(True,False))

    if int(dato) > 5 :
        print("mayor: ",a)
    else:
        print("Mayor: ",b)    
    print(potencia.format(dato,int(dato)**2))
    print(2&6)
except:
  print("Ocurrió un error")

