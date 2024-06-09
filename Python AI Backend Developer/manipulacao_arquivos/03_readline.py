arquivo = open("file.txt", "r")

for linha in arquivo.readlines():
    print(linha, end='')

# tip
# while linha := arquivo.readline():
#     print(linha, end='')
arquivo.close()
