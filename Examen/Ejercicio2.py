import re

txt = "Hola"
text2 = "Hola Mundo"
x = re.search(txt,text2)


ini = x.span()[0] #posición inicial de la subcadena
fin = x.span()[1]
subcadena = txt[ini:fin]


print(subcadena)