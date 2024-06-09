class MeuIterador:
    def __init__(self, numeros):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            posicao = self.numeros[self.contador]
            self.contador += 1
            return posicao

        except IndexError:
            raise StopIteration


for i in MeuIterador([10, 20, 30]):
    print(i)
