numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# v1
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

# v2
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)
