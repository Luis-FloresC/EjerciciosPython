

listaAbecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                           "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
      
def convertCadenaOnList(cadena):
    cadena_Lista = []
    for letra in cadena:
        cadena_Lista.append(letra)
    return cadena_Lista


print(convertCadenaOnList("XYZ"))      

encrip = input("Ingrese el codigo: ")
palabra = encrip.lower().split(" ")
caja = ['murcielago','hipotenusa','escupitajo','sudorienta','bisabuelos','riachuelos','bufonerias','questionar','suponieras','autenticos']
encriptacion = []
for letra in palabra:
    word = ""
    enc = ""
    indice = 0
    indexL = 0
    m = 0
    for palabra in caja:
        coinci = 0
        for i in range(len(letra)):
            if (letra[i] in palabra):
                coinci += 1
        if (coinci > m):
            m = coinci
            word = palabra
    for i in range(len(caja)):
        if (word == caja[i]):
            indice = i
    enc = str(indice)
    for j in letra:
        indexL = ""
        for i in range(len(word)):
            if (j == word[i]):
                indexL += str(i)
        if (j not in word):
            indexL += j.upper()
        enc += indexL
    encriptacion.append(enc)
print(" ".join(encriptacion))