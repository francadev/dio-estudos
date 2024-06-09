pessoa1 = {"nome": "Rafael", "idade": 25, "sexo": None}
pessoa2 = dict(nome="Guilherme", idade=28)

# novas chaves adicionam novos valores caso ainda não existam
pessoa1["telefone"] = "9999-9999"
print(pessoa1)
print(pessoa1["sexo"])

pessoa2["nome"] = "Luh"
print(pessoa2["nome"])
