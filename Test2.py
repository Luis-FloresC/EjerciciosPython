a = int(input("Ingrese su edad: "))

if a > 60:
    print("Es de la tercera edad...")
elif a >= 18:
    print("Es Mayor de edad...")
else:
    print("No es Mayor de edad...")    

datos = ["Perro","Gato","Mono"]

for dato in datos:
    print(dato)
mensaje = "El numero {0}: {1}"
isPrimo = False
if a == 0 or a == 1 or a == 4:
    isPrimo = False  
else:
    for n in range(2,a-1):
        if n % a == 0:
            isPrimo = True
            break;     
      

if isPrimo:
   print(mensaje.format(a,"Es primo"))  
else:
   print(mensaje.format(a,"No es primo"))     
   
   
es_bonito = True
estado = "Es bonito" if es_bonito else "No es bonito" 
print(estado)  
          