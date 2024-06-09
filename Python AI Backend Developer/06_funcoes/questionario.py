def funcao(titulo, *args, **kw):
    print(args, kw)
    print(titulo)


funcao("Python", "python", 2022, curso="dio")