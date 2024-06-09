def meu_decorador(funcao):
    def envelope():
        print("Executando antes da função...")
        funcao()
        print("Executando depois da função...")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


meu_decorador(ola_mundo())
