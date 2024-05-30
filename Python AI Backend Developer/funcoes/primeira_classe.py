def somar(a, b):
    return a + b


def exibir_resultado(a, b):
    resultado = somar(a, b)
    print(resultado)


def exibir_resultado_function(a, b, funcao):
    resultado = funcao(a, b)
    print(resultado)


resultado = somar

exibir_resultado(10, 20)
exibir_resultado_function(21, 29, somar)
print(resultado(10, 10))
