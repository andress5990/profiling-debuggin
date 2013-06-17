# -*- coding: UTF-8 -*-

import funciones_intro
import numpy as np
import pytest

numeros = np.random.random(100)

def test_mi_promedio_resultado_correcto():
    # Valida el resultado comparando con el average de numpy
    prom_np = np.average(numeros)
    assert prom_np == funciones_intro.mi_promedio(numeros)

def test_mi_promedio_falla_cero():
    with pytest.raises(ZeroDivisionError):
        funciones_intro.mi_promedio([])
