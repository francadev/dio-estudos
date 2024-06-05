class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def get_nome(self):
        return self.nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self.ano_nascimento


pessoa = Pessoa("Rafael", 1998)
print(pessoa.idade)
