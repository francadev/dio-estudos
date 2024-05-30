contatos = {
    "nome": "Rafael", "telefone": "9999-9999"
}

# adiciona valor caso não exista
contatos.setdefault("nome", "Giovana")
print(contatos)

contatos.setdefault("idade", 25)
print(contatos)
