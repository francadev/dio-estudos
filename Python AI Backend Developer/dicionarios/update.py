contatos = {
    "Rafael": {"idade": 25, "celular": "9999-9999"},
    "Luh": {"idade": 27, "celular": "8888-8888"}
}

print(contatos)
contatos.update({"Rafael": {"idade": 25}})
print(contatos)

resultado = "Luh" in contatos
print(resultado)

resultado = "celular" in contatos["Rafael"]
print(resultado)
