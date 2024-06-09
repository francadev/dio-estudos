curso = "pYtHon"

# uso de interpolação para print
print(f'Todas as letras em maiúsculo: "{curso.upper()}"')
print(f'Todas as letras em minúsculo: "{curso.lower()}"')
print(f'Apenas a primeira letra em maiúsculo: "{curso.title()}"')


curso = "   Python     teste    "
print(f'Corta os espaços em branco no início e no fim da palavra ou frase: "{curso.strip()}"')
print(f'Apaga qualquer caractere branco apenas no INÍCIO da palavra ou frase: "{curso.lstrip()}"')

curso = "Oi Oi"
print(f"Padroniza o tamanho da string adicionando caracteres na palavra: {curso.center(10, '#')}")

curso = "Python Python"
print(f"Após cada um dos caracteres, adicione outro: {' '.join(curso)}")

curso = "Python"
print("-".join(curso))
for letra in curso:
    print(letra, end='-')
