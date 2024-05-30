salario_original = 5000


def salario_bonus(bonus):
    global salario_original
    novo_salario = salario_original
    novo_salario += bonus
    print("novo_salario", novo_salario)


salario_bonus(500)
print("salario_original", salario_original)
