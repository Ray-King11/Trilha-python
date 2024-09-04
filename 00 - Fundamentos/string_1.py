# Maiúscula, minúscula e título
nome = "gUIlherME"

print(nome.upper()) # Maiúscula
print(nome.lower()) # Minúscula
print(nome.title()) # Título


# Eliminado espaços em branco
texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") # Remove espaços ou caracteres especificado do inicio e do final da string
print(texto.rstrip() + ".") # Remove espaços ou caracteres especificado apenas do final da string, da direita para esquerda
print(texto.lstrip() + ".") # Remove espaços ou caracteres especificado apenas do inicio da string, da esquerda para direita


# Junção e centralização
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu)) # .join usado para acrescentar ou concatenar elementos de um interável no meio de uma strig
