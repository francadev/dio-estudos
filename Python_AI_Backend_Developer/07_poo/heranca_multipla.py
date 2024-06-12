class Animal:
    def __init__(self, cor):
        self.cor = cor

    def som(self):
        print("Som indefinido...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico


class Mamifero(Animal):
    def __init__(self, nro_patas, **kwargs):
        super().__init__(**kwargs)
        self.nro_patas = nro_patas


class Gato(Animal):
    def som(self):
        print("Miau!")


class Cachorro(Animal):
    def __init__(self, cor, dono):
        super().__init__(cor)
        self.dono = dono

    def tem_dono(self):
        print(f"{'Sim,' if self.dono else 'Não'} tem dono.")


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor, cor_bico, nro_patas):
        super().__init__(cor=cor, cor_bico=cor_bico, nro_patas=nro_patas)


ave = Ave(cor="Azul", cor_bico="Cinza")
print(ave)

mamifero = Mamifero(cor="Marrom", nro_patas=4)
print(mamifero)

perry = Ornitorrinco(cor="Verde", cor_bico="Preto", nro_patas=2)
print(perry)
