contatos = {
    "Rafael": {"celular": "9999-9999", "email": "francadev9@gmail.com", "endereço": {"rua": "rua 1", "número": 10}},
    "Luh": {"celular": "8888-8888", "email": "luh@gmail.com", "endereço": {"rua": "rua 2", "número": 20}}
}
contatos2 = contatos.copy()

sexo = contatos2.get("sexo")
print(sexo)

# não retorna erro se não existe, retornando None por padrão
sobrenome = contatos2.get("sobrenome")
print(sobrenome)

# não retorna erro se não existe, retornando None por padrão. Se não existe, retorne o valor especificado
sobrenome = contatos2.get("sobrenome", "Carvalho")
print(sobrenome)
