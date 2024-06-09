def etapas():
    def funcao(n):
        n += 1
        return f'Executando etapa {n}', n

    def acabou():
        return 'Acabou!'

    n = 0
    yield funcao(n)
    yield funcao(n)
    yield acabou()


gen = etapas()
print(next(gen))
print(next(gen))
print(next(gen))
