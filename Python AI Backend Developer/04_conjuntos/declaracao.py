# ide sugere o uso de {} ao invés de set()
conjunto1 = {1, 2, 3, 4, 5, 2, "oi", "teste"}
conjunto2 = set('abacaxi')

print(conjunto1, type(conjunto1))
print(conjunto2, type(conjunto2))

conjunto_vazio = set()
dicionario_vazio = {}
print("conjunto_vazio", type(conjunto_vazio))
print("dicionario_vazio", type(dicionario_vazio))

conjunto3 = ['py', 'py', 'thon']
conjunto3 = set(conjunto3)
print(conjunto3)

conjunto3.add('thon')
print(conjunto3)
