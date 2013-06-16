# -*- coding: UTF-8 -*-

import funciones_intro
import numpy as np

from nose.tools import *

numeros = np.random.random(100)

@raises(ZeroDivisionError)
def test_mi_promedio_falla_cero():
    # Valida que la funcion falle cuando la lista de numeros está vacia
    funciones_intro.mi_promedio([])

def test_mi_promedio_resultado_correcto():
    # Valida el resultado comparando con el average de numpy
    prom_np = np.average(numeros)
    assert prom_np == funciones_intro.mi_promedio(numeros)

def test_mi_promedio_uno_no_es_primo():
    # Valida que la función sepa que el 1 no es un numero primero
    assert not funciones_intro.es_primo(1)

def test_negativos_no_son_primos():
    # Valida que numeros negativos no se consideren como primos
    assert not funciones_intro.es_primo(-1)

@raises(TypeError)
def test_crash_con_no_numerico():
    # Valida que la función falle ante un parámetro no numérico
    funciones_intro.es_primo("no soy un numero")

@raises(ValueError)
def test_parametro_falla_valor_menor_minimo():
    # Valida que falle con Value error si el valor dado está por debajo del minimo permitido
    funciones_intro.es_bisiesto(1899)

@raises(ValueError)
def test_parametro_falla_valor_menor_maximo():
    # Valida que falle con Value error si el valor dado está por debajo del máximo permitido
    funciones_intro.es_bisiesto(2501)

