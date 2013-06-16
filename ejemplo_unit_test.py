# -*- coding: UTF-8 -*-

import funciones_intro
import numpy as np
import unittest

# Clase para pruebas a la funcion mi_promedio
class TestPromedio(unittest.TestCase):

    def setUp(self):
        # Metodo similar al constructor donde se inicializan datos de prueba
        self.numeros = np.random.random(100)

    def test_falla_cero(self):
        # Valida que la funcion falle cuando la lista de numeros está vacia
        self.assertRaises(ZeroDivisionError, funciones_intro.mi_promedio, [])

    def test_resultado_correcto(self):
        # Valida el resultado comparando con el average de numpy
        prom_np = np.average(self.numeros)
        self.assertEqual(prom_np, funciones_intro.mi_promedio(self.numeros))


# Clase para pruebas a la funcion es_primo
class TestEsPrimo(unittest.TestCase):

    def test_uno_no_es_primo(self):
        # Valida que la función sepa que el 1 no es un numero primero
        self.assertFalse(funciones_intro.es_primo(1))

    def test_negativos_no_son_primos(self):
        # Valida que numeros negativos no se consideren como primos
        self.assertFalse(funciones_intro.es_primo(-1))

    def test_crash_con_no_numerico(self):
        # Valida que la función falle ante un parámetro no numérico
        self.assertRaises(TypeError, funciones_intro.es_primo, "no soy un numero")

# Clase para pruebas a la funcion es_bisiesto
class TestBisiesto(unittest.TestCase):

    def test_parametro_falla_valor_menor_minimo(self):
        # Valida que falle con Value error si el valor dado está por debajo del minimo permitido
        self.assertRaises(ValueError, funciones_intro.es_bisiesto, 1899)

    def test_parametro_falla_valor_menor_maximo(self):
        # Valida que falle con Value error si el valor dado está por debajo del máximo permitido
        self.assertRaises(ValueError, funciones_intro.es_bisiesto, 2501)


# Ejecuta las pruebas
unittest.main()