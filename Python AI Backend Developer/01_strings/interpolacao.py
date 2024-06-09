import math

frase = "Eu estou estudando {}"
print(frase.format("Python"))
print(f"Eu estou estudando {'Python'}")

nome = "Rafael"
idade = 25
profissao = "Programador"
linguagem = "Python"
print("Me chamo {} e tenho {} anos. Trabalho como {} utilizando a linguagem {}.".format(nome, idade, profissao,
                                                                                        linguagem))
print("Me chamo {0} e tenho {2} anos. Trabalho como {1} utilizando a linguagem {3}.".format(nome, profissao, idade,
                                                                                            linguagem))

print("Me chamo {nome} e tenho {idade} anos. Trabalho como {profissao} utilizando a linguagem {linguagem}.".format(
      nome=nome, profissao=profissao, idade=idade, linguagem=linguagem))

print(f"Me chamo {nome} e tenho {idade} anos. Trabalho como {profissao} utilizando a linguagem {linguagem}.")

PI = math.pi
print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")

dados = {"nome": "Rafael", "idade": 25}
print("Me chamo {nome} e tenho {idade} anos.".format(**dados))
