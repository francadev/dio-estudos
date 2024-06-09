class MeuIterador:
    def __init__(self, file_name):
        self.file_name = open(file_name, 'r')

    def __iter__(self):
        return self.file_name

    def __next__(self):
        file_line = self.file_name.readline()
        if line != '':
            return file_line
        else:
            self.file_name.close()
            raise StopIteration


for line in MeuIterador('file.txt'):
    print(line, end='')
