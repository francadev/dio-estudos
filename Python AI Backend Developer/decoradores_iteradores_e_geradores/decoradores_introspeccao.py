import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope():
        print("Executando antes da função...")
        funcao()
        print("Executando depois da função...")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


# a funcao permanece com o seu nome
print(ola_mundo.__name__)


ola_mundo()
