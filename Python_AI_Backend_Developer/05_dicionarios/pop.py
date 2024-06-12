contatos = {
    "Rafael": {"celular": "9999-9999", "email": "francadev9@gmail.com", "endereço": {"rua": "rua 1", "número": 10}},
    "Luh": {"celular": "8888-8888", "email": "luh@gmail.com", "endereço": {"rua": "rua 2", "número": 20}}
}

print(contatos)

# retorna o valor removido ou a mensagem caso não encontrado
resultado = contatos.pop("Sandra", "Não encontrado")
print(resultado)
print(contatos)
