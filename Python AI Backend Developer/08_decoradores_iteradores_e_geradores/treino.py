def generator(lista):
    for i in lista:
        yield i


gen = generator([1, 2, 3])
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
