import PyPDF2 as pdf
from PyPDF2 import PdfReader

# 1 - Versão e Métodos dessa Biblioteca
# print(pdf.__version__)
# print(dir(pdf))

# 2 - Importando arquivo PDF
file = open('files/arte_da_guerra.pdf', 'rb')
reader = PdfReader(file)
print(reader)
print(reader.metadata)
info = reader.metadata

# 3 - Extraindo algumas informações
print(info.title)
print(info.author)
print(info.creator)
print(info.subject)
print(len(reader.pages))
print(reader.pages[15].extract_text())