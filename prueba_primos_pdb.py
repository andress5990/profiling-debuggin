#!/usr/bin/python
# -*- coding: UTF-8 -*-

from funciones_intro import es_primo

import pdb

def revisar_primos(numeros):
    cantidad = 0
    for n in numeros:
        if es_primo(n):
            cantidad += 1
            print "El numero %d es primo" % (n)

    return cantidad

# Defino una lista vacia
lista = []

print "Ingrese numeros para la lista. Cuando quiera parar, digite stop"

while True:
    cadena = raw_input()
    # Define un breakpoint. El programa se detendrá aquí
    pdb.set_trace()
    if cadena == "stop":
        break
    else:
        try:
            lista.append(int(cadena))
        except ValueError:
            print "El valor %s no es un numero! " % (cadena)

cantidad = revisar_primos(lista)

print "La cantidad de numeros primos encontrados fue: %d" % (cantidad)
