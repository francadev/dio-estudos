def meu_decorador(funcao):
    def envelope():
        print("Executando antes da função...")
        funcao()
        print("Executando depois da função...")

    return envelope


def ola_mundo():
    print("Olá mundo!")


ola_mundo_decorador = meu_decorador(ola_mundo)
ola_mundo_decorador()
