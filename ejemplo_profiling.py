# -*- coding: UTF-8 -*-

import time
import timeit

def calcular_pi(nmax):
	i = 1	# contador para el ciclo
	producto = 1	#lleva el resultado de la productoria
	while i <= nmax:
		producto *= (4. * i ** 2) / ((2 * i - 1) * (2 * i + 1))
		i += 1
	return producto*2

# Profiling basico
def profile_time():
    start = time.time()
    resultado = calcular_pi(1000000)
    end = time.time()
    diff = end - start
    print "La ejecución tomó %.5fs. Resultado: %s - Medida con time" % (diff, resultado)

# Profiling con timeit
def profile_timeit():
    N = 100
    time_ms = timeit.timeit("calcular_pi(1000000)", "from __main__ import calcular_pi",
                  number=N)
    print "La ejecución tomó %.5fs" % (time_ms/N)

profile_time()
profile_timeit()
