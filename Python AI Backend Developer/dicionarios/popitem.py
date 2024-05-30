contatos = {
    "Rafael": {"celular": "9999-9999", "email": "francadev9@gmail.com", "endereço": {"rua": "rua 1", "número": 10}},
    "Luh": {"celular": "8888-8888", "email": "luh@gmail.com", "endereço": {"rua": "rua 2", "número": 20}}
}

# exclui o último valor, se acabarem as chaves: key error
contatos.popitem()
print(contatos)
