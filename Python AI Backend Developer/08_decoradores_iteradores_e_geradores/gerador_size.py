import sys


lista = [numero for numero in range(1000)]
generator = (numero for numero in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(next(generator))
print(next(generator))
