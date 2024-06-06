class Estudante:
    universidade = "IFSP"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome, self.matricula, self.universidade}"


def mostrar_valores(*args):
    for arg in args:
        print(arg)


aluno_1 = Estudante("Rafael", "99")
aluno_2 = Estudante("Luh", "88")

mostrar_valores(aluno_1, aluno_2)
Estudante.universidade = "DIO"
mostrar_valores(aluno_1, aluno_2)
aluno_2.universidade = "SENAC"
mostrar_valores(aluno_1, aluno_2)
