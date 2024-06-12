import textwrap


def menu_principal():
    menu = """
    Selecione a opção desejada:

    [d]  Depositar
    [s]  Sacar
    [e]  Ver extrato 
    [u]  Criar usuário
    [c]  Criar conta
    [vu] Ver usuários
    [vc] Ver Contas
    [q]  Sair

    Opção escolhida: """
    return input(textwrap.dedent(menu))


def menu_criar_usuario():
    menu = """
    Você ainda ainda não está cadastrado para criar uma conta. Selecione a opção desejada:

    [u]  Criar apenas usuário
    [uc] Criar usuário e conta
    [v]  Voltar para o menu principal


    Opção escolhida: """
    return input(textwrap.dedent(menu))


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor < saldo and numero_saques < limite_saques and valor <= limite:
        saldo -= valor
        numero_saques += 1
        extrato.append(("Saque", valor))
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo: .2f}")
    elif numero_saques >= limite_saques:
        print(f"Limite de saque atingido. Já foram realizados {numero_saques} saques.")
    elif numero_saques > limite:
        print(f"O valor máximo de saque é de R$ {limite: .2f}")
    else:
        print(f"Saldo insuficiente para realizar a operação!\nSeu saldo atual é R$ {saldo}")
    return saldo, numero_saques


def deposito(saldo, valor, extrato, /):
    if valor >= 10:
        saldo += valor
        extrato.append(("Depósito", valor))
        print(f"Valor depositado com sucesso! Saldo atual: R$ {saldo: .2f}")
    elif valor < 0:
        print("É impossível depositar um valor negativo.")
    else:
        print("Valor mínimo de deposito: R$ 10,00.")
    return saldo, extrato


def ver_extrato(saldo, /, *, extrato):
    if len(extrato) > 1:
        print(f"### VER EXTRATO ###\nSaldo inicial: R$ {extrato[0][1]: .2f}")
        for operacao, valor in extrato:
            if operacao != "Saldo inicial":
                extrato_wrap = textwrap.dedent(f"""
                    Operação realizada: {operacao}
                    Valor: R$ {valor: .2f}""")
                print(extrato_wrap)
        print(f"\nSaldo final: R$ {saldo: .2f}\n### FIM DO EXTRATO ###")
    else:
        print("Nenhuma movimentação realizada!")


def criar_usuario(usuarios, cpf=None):
    if not cpf:
        cpf = input("Insira o CPF: ")
        usuario_cadastrado = buscar_usuario(usuarios, cpf)
        if usuario_cadastrado:
            print("Este CPF já está cadastrado!")
            return
    nome = input("Insira o seu nome: ")
    data_nascimento = input("Insira a data de nascimento: ")
    endereco = input("Insira o endereço: ")
    novo_usuario = {"cpf": cpf, "nome": nome, "data_de_nascimento": data_nascimento, "endereco": endereco}
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return novo_usuario


def buscar_usuario(usuarios, cpf):
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_encontrado[0] if usuario_encontrado else None


def criar_conta(contas, agencia, usuarios):
    cpf = input("Para criar uma conta, insira o CPF: ")
    usuario_encontrado = buscar_usuario(usuarios, cpf)
    if not usuario_encontrado:
        while True:
            opc = menu_criar_usuario()
            if opc == 'uc':
                novo_usuario = criar_usuario(usuarios, cpf)
                contas.append({"agencia": agencia, "numero_da_conta": len(contas) + 1, "usuario": novo_usuario})
                print("Conta criada com sucesso!")
                return
            elif opc == 'u':
                criar_usuario(usuarios, cpf)
                return
            elif opc == 'v':
                break
            else:
                print("Opção inexistente, digite uma opção existente.")
                continue

    contas.append({"agencia": agencia, "numero_da_conta": len(contas) + 1, "usuario": usuario_encontrado})
    print("Conta criada com sucesso!")


def ver_contas(contas):
    if contas:
        print(f"### VER CONTAS ###")
        for conta in contas:
            conta_wrap = textwrap.dedent(f"""
            Agência: {conta["agencia"]}
            Número da conta: {conta["numero_da_conta"]}
            CPF: {conta["usuario"]["cpf"]}
            Nome: {conta["usuario"]["nome"]}
            Data de nascimento: {conta["usuario"]["data_de_nascimento"]}
            Endereço: {conta["usuario"]["endereco"]}""")
            print(conta_wrap)
        print(f"\n### FIM DAS CONTAS ###")
    else:
        print("Nenhuma conta cadastrada!")


def ver_usuarios(usuarios):
    if usuarios:
        print(f"### VER USUÁRIOS ###")
        for usuario in usuarios:
            usuario_wrap = textwrap.dedent(f"""
                CPF: {usuario["cpf"]}
                Nome: {usuario["nome"]}
                Data de nascimento: {usuario["data_de_nascimento"]}
                Endereço: {usuario["endereco"]}""")
            print(usuario_wrap)
        print(f"\n### FIM DOS USUÁRIOS ###")
    else:
        print("Nenhum usuário cadastrado!")


def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = [("Saldo inicial", saldo)]
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opc = menu_principal()
        if opc == 'd':
            try:
                saldo, extrato = deposito(saldo,
                                          int(input("Digite o valor a ser depositado: R$ ")),
                                          extrato)
            except ValueError:
                print("Digíte apenas números...")
                continue

        elif opc == 's':
            try:
                saldo, numero_saques = saque(saldo=saldo,
                                             valor=int(input("Digite o valor a ser sacado: R$ ")),
                                             extrato=extrato,
                                             limite=limite,
                                             numero_saques=numero_saques,
                                             limite_saques=LIMITE_SAQUES)
            except ValueError:
                print("Digíte apenas números...")
                continue

        elif opc == 'e':
            ver_extrato(saldo, extrato=extrato)

        elif opc == 'u':
            criar_usuario(usuarios)

        elif opc == "c":
            criar_conta(contas, AGENCIA, usuarios)

        elif opc == 'q':
            print("Saindo do programa bancário...")
            break

        elif opc == 'vu':
            ver_usuarios(usuarios)

        elif opc == 'vc':
            ver_contas(contas)

        else:
            print("Opção inexistente, digite uma opção existente.")
            continue


main()
