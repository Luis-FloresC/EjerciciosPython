import os
import os.path as path
from pip._vendor.distlib.compat import raw_input

nombreArchivo = "Estudiante.txt"
Estdiante = list()

Existe = False
def CreacionArchivo():
    if path.exists(nombreArchivo):
        
        Existe = True
    else:
         
        Existe = False
    return Existe     

def ValidarOpcion(valor,li,ls):
    while(valor < li or valor > ls):
        print(f"Ingrese una opcion valida entre [{li}] / [{ls}]...")
        valor = int(input("Ingrese su Opcion: "))
    return valor

def ValidarOpcionLetra(valor,li,ls):
    while(valor != li and valor != ls):
        print(f"Ingrese una opcion valida entre [{li}] / [{ls}]...")
        valor = input("Ingrese su Opcion: ")
        valor = valor.upper()
    return valor

Tabla = ""
def IngresarDatos():
    while True:
        os.system("Cls")
        print(f"*** Ingresar Datos Generales del Alumno ***\n")
        NombreCompleto = input(f"Ingrese el Nombre Completo del Alumno: ")
        Edad = int(input(f"Ingrese su edad: "))
        Universidad = input(f"Ingrese la Universidad: ")
        telefono = input("Ingrese su Telefono: ")
   
        Estdiante.append([NombreCompleto,Edad,Universidad,telefono]) 
        Respuesta = input("Desea Continuar: SI / NO: ")
        Respuesta = Respuesta.upper()
        Respuesta = ValidarOpcionLetra(Respuesta,"SI","NO")
       
        Archivo = open(nombreArchivo,"a")
        Tabla = (('\n'.join("| {:<18} | {:<15} | {:<15} | {:<15} |".format(*fila) for fila in Estdiante)))
    
        Archivo.write(Tabla)
        Archivo.write("\n")
        Archivo.close()   
        Estdiante.clear()
        if(Respuesta == "NO"):
            break
    
    
if(CreacionArchivo() == True):
    Archivo = open(nombreArchivo,"a")
    
    # print("El Archivo ya existe...")
else:
    Archivo = open(nombreArchivo,"w")
    Cadena = "| {:<18} | {:<15} | {:<15} | {:<15} |\n"
    Archivo.write(Cadena.format("Nombre Completo","Edad","Universidad","Telefono"))
    print("El Archivo se creo Exitosamente")  
    Archivo.close()


opcion = 0

while opcion != 3:
    try:
        os.system("Cls")
        print("\t\t*** Menu Principal ***")
        print("-"*55)
        print("1- Ingresar Datos Generales de un Pais")
        print("2- Mostrar Datos Generales")
        print("3- Salir")
        print("-"*55)
        opcion = int(input("Ingrese una Opcion: "))
    
        opcion = ValidarOpcion(opcion,1,3)
        if opcion == 1:
            
            IngresarDatos()
       

        elif opcion == 2:
            os.system("Cls")
            Archivo = open(nombreArchivo,"r")
            print(Archivo.read())
        else:
            break;    

    except ValueError:
        print("Ocurrio un Error,Vuleva a Intentar")
        opcion = 0
    finally:
        raw_input('presione la tecla enter para continuar...')
        Archivo.close()