lista1 = []
lista1.append(1)
lista1.append('py')
lista1.append('py')
lista1.append([40, 30, 20])
print('lista1=', lista1)
lista2 = lista1.copy()

lista1.clear()
print('lista1=', lista1)
print('lista2=', lista2)

print(id(lista1))
print(id(lista2))

print(lista2.count('py'))

print('lista2=', lista2)
lista2.extend(['test', 'extend'])
print('lista2=', lista2)

print(lista2.index('py'))
lista2.remove(lista2[1])
lista2.extend(['test', 'extend'])
print('lista2=', lista2)

lista2.pop()
print('lista2=', lista2)
lista2.pop(0)
print('lista2=', lista2)

lista2.remove('test')
print('lista2=', lista2)

# ordenar por tamanho
# método
lista3 = ["python", "js", "c", "java", "csharp"]
lista3.sort(key=lambda x: len(x))
print(lista3)
# função
print(sorted(lista3, key=lambda x: len(x)))
