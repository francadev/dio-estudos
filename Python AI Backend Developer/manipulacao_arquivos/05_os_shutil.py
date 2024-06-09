import shutil
import os
from pathlib import Path


ROOT_PATH = Path(__file__).parent
novo_diretorio = Path(__file__).parent / 'novo-diretorio'


# os.mkdir(novo_diretorio)
# arquivo = open(novo_diretorio / 'new_file.txt', 'w')
# arquivo = open(novo_diretorio / 'other_new_file.txt', 'w')
# arquivo.close()

# os.rename(novo_diretorio / 'new_file.txt', novo_diretorio / 'other.txt')
# os.remove(novo_diretorio / 'other.txt')

shutil.move(novo_diretorio/'new_file.txt', ROOT_PATH)
