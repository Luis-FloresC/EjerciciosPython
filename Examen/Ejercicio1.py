import math

ListEntero = [72,60,54,42]


def CalcularMCD(num1,num2):
    return math.gcd(num1,num2);

def CalcularListaDeEnteros(n):
    ListNum = list(n)
    ResultMCD = CalcularMCD(ListNum[0], ListNum[1])
    if len(ListNum) > 2:
        for n in ListNum[2:]:
            ResultMCD = CalcularMCD(ResultMCD, n)
    return (ResultMCD)

print(ListEntero)
print("MCD: ",CalcularListaDeEnteros(ListEntero))
