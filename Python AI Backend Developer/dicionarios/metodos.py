contatos = {
    "Rafael": {"celular": "9999-9999", "email": "francadev9@gmail.com", "endereço": {"rua": "rua 1", "número": 10}},
    "Luh": {"celular": "8888-8888", "email": "luh@gmail.com", "endereço": {"rua": "rua 2", "número": 20}}
}

contatos2 = contatos.copy()

print(contatos)
print(contatos2)

contatos2.clear()
print(contatos2)

# limpa e cria chaves sem valor (None)
contatos2 = dict.fromkeys(["sobrenome", "idade"])
print(contatos2)

# limpa e cria chaves com um valor específico
contatos2 = contatos2.fromkeys(["sexo"], "vazio")
print(contatos2)

sexo = contatos2.get("sexo")
print(sexo)

# não retorna erro se não existe, retornando None por padrão
sobrenome = contatos2.get("sobrenome")
print(sobrenome)

# não retorna erro se não existe, retornando None por padrão. Se não existe, retorne o valor especificado
sobrenome = contatos2.get("sobrenome", "Carvalho")
print(sobrenome)
