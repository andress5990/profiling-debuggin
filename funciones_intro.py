#!/usr/bin/python
# -*- coding: UTF-8 -*-


def es_primo(n):
    if n <= 1:
        return False
    contador = 2
    while contador < n:
        if n % contador == 0:
            return False
        contador+= 1
    #Si llegue a este punto, se que el numero es primo
    return True

def es_bisiesto(n):

    if n < 1900 or n > 2500:
        raise ValueError("El rango valido es de 1900 ad 2500")

    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def mi_promedio(numeros):
    acumulado = 0
    longitud = len(numeros)
    for n in numeros:
        acumulado += n

    return acumulado / longitud