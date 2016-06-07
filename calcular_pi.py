import sys

def wallis(n):
    factor1 = (2*n) / float(2*n - 1)
    factor2 = (2*n) / float(2*n + 1)

    return factor1 * factor2


try:
    n = int(sys.argv[1])
except IndexError:
    print "Debe indicar un parametro n"
    exit()
except ValueError:
    print "El n debe ser un numero"
    exit()

resultado = 1

for i in range(1, n+1):
    resultado *= wallis(i)

resultado *= 2

print 'El resultado es: ', resultado
