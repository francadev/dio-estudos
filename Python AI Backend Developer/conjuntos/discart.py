conjunto = {1, 2, 3, 4, 5}
print(conjunto)

conjunto.discard(2)
print(conjunto)

# não dá erro caso não encontre o elemento
conjunto.discard(20)
print(conjunto)

# remove o primeiro valor (lista remove o último)
conjunto.pop()
print(conjunto)

# remove o valor especificado (se não existe dá erro)
conjunto.remove(5)
print(conjunto)

conjunto.add(20)
print(conjunto)
