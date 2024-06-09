try:
    with open('files.txt', 'r') as file:
        print(file.read())

except IOError as err:
    print(f'Erro ao abrir o arquivo: {err}')


try:
    with open('aprendendo.txt', 'w', encoding='utf-8') as file:
        file.write("Aprendendo a manipular arquivos...")

except IOError as err:
    print(f'Erro ao abrir o arquivo: {err}')
