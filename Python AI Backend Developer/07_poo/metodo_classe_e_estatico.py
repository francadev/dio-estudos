class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, nome, ano_nascimento):
        idade = 2024-ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento("Rafael", 1998)
print(p.idade)
print(p.maior_idade(17))
