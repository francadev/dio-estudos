class Animal:
    def __init__(self, cor):
        self.cor = cor

    def som(self):
        print("Som indefinido...")

    def __str__(self):
        return f"{self.__class__.__name__}: {''.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Gato(Animal):
    def som(self):
        print("Miau!")


class Cachorro(Animal):
    def __init__(self, cor, dono):
        super().__init__(cor)
        self.dono = dono

    def tem_dono(self):
        print(f"{'Sim,' if self.dono else 'Não'} tem dono.")


c = Cachorro("Preto", False)
c.som()
c.tem_dono()

# g = Gato("Branco")
# g.som()
# print(g)
