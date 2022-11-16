from typing import Callable, Any


def multiplica(*multiplicante):
    "Multiplica infinitos argumentos teste"
    resultado = 1
    for number in multiplicante:
        resultado = number * resultado

    return resultado


print(multiplica(10, 5, 2,7,6,4,9))
print(multiplica.__doc__)
