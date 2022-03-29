from shlex import join
from tokenize import String



ls = ["Hola","Mundo","Loco"]
lsString = '-'.join(ls)
print(lsString)

listaStr = lsString.split('-')
print(listaStr)
