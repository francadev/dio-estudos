<<<<<<< HEAD
=======
# não permite valores negativos, todos depósitos devem ser armazenados em uma variável e exibidos no extrato
# o sistema deve permitir até 3 saques diários de no máximo 500.
# O objetivo é implementar três operações essenciais: depósito, saque e extrato.
# no extrato deve ter o tipo e o valor da operação

>>>>>>> 0d9ca4e (feat: Criando um Sistema Bancário com Python)
menu = """
Selecione a opção desejada:

[d] Depositar
[s] Sacar
[e] Ver extrato 
[q] Sair

Opção escolhida: """

saldo = 0
limite = 500
extrato = [("Saldo inicial", saldo)]
numero_saques = 0
LIMITE_SAQUES = 3
SAQUE_MAX = 500


def saque(valor):
    global saldo
    global numero_saques
    if valor < saldo and numero_saques < LIMITE_SAQUES and valor <= SAQUE_MAX:
        saldo -= valor
        numero_saques += 1
        extrato.append(("Saque", valor))
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo: .2f}")
    elif numero_saques >= LIMITE_SAQUES:
        print(f"Limite de saque atingido. Já foram realizados {numero_saques} saques.")
    elif numero_saques > SAQUE_MAX:
        print(f"O valor máximo de saque é de R$ {SAQUE_MAX: .2f}")
    else:
        print(f"Saldo insuficiente para realizar a operação!\nSeu saldo atual é R$ {saldo}")


def deposito(valor):
    global saldo
    if valor >= 10:
        saldo += valor
        extrato.append(("Depósito", valor))
        print(f"Valor depositado com sucesso! Saldo atual: R$ {saldo: .2f}")
    elif valor < 0:
        print("É impossível depositar um valor negativo.")
    else:
        print("Valor mínimo de deposito: R$ 10,00.")


while True:
    opc = input(menu)
    if opc == 'd':
        try:
            deposito(int(input("Digite o valor a ser depositado: R$ ")))
        except ValueError:
            print("Digíte apenas números...")
            continue

    elif opc == 's':
        try:
            saque(int(input("Digite o valor a ser sacado: R$ ")))
        except ValueError:
            print("Digíte apenas números...")
            continue

    elif opc == 'e':
        print(f"### VER EXTRATO ###\nSaldo inicial: R$ {extrato[0][1]: .2f}")
        for operacao, valor in extrato:
            if operacao != "Saldo inicial":
                print(f"""
        Operação realizada: {operacao}
        Valor: R$ {valor: .2f}""")
        print(f"\nSaldo final: R$ {saldo: .2f}\n### FIM DO EXTRATO ###")

    elif opc == 'q':
        print("Saindo do programa bancário...")
        break

    else:
        print("Opção inexistente, digite uma opção existente.")
        continue
