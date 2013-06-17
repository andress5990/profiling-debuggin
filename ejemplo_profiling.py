# -*- coding: UTF-8 -*-

import time
import timeit

def raiz_newton(x, err, verbose=False):
    resultado = x/2.0
    while(True):
        cociente = x / resultado
        promedio = (resultado + cociente) / 2.0
        diferencia = abs(promedio - resultado)
        resultado = promedio
        if verbose:
            print "Estimado: %s - Cociente: %s - Promedio: %s - Diff: %s" % (str(resultado),
                                                                             str(cociente)[:5], str(promedio)[:5], str(diferencia))
        if diferencia < err:
            break

    return resultado


# Profiling basico
def profile_time():
    start = time.time()
    resultado = raiz_newton(3487348343, 1E-8)
    end = time.time()
    diff = end - start
    print "La ejecución tomó %.5fs. Resultado: %s - Medida con time" % (diff, resultado)

# Profiling con timeit
def profile_timeit():
    N = 100000
    time_ms = timeit.timeit("raiz_newton(3487348343, 1E-8)", "from __main__ import raiz_newton",
                  number=N)
    print "La ejecución tomó %.5fs" % (time_ms/N)

profile_time()
profile_timeit()