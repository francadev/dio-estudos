conjunto_a = {1, 2}
conjunto_b = {2, 3, 4}
print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

# a faz parte de b? b faz parte de a?
print()
conjunto_a = {1, 2}
conjunto_b = {1, 2, 3, 4}
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# tem intersecção?
print()
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5}
print(conjunto_a.isdisjoint(conjunto_b))
