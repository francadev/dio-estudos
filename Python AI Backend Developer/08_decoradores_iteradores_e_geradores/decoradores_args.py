def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Executando antes da função...")
        funcao(*args, **kwargs)
        print("Executando depois da função...")

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá, {nome}!")


meu_decorador(ola_mundo("Rafael"))
