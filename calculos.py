#modulo con funciones para pi y raiz

def calcular_pi(nmax):
	i = 1	#contador para el ciclo
	producto = 1	#lleva el resultado de la productoria
	while i <= nmax:
		producto *= (4. * i ** 2) / ((2 * i - 1) * (2 * i + 1))
		i += 1
	return producto*2

def raiz_newton(x, err):
	est = 1.0	#estimado
	dif = 1.0	#diferencia
	while dif > err:
		coc = x / est	#cociente
		prom = (est + coc) / 2.0	#promedio
		dif = abs(est-prom)
		est = prom	#nueva estimacion es el resultado anterior
	return prom






