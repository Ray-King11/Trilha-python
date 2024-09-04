
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# range(stop) -> range object
# range(start, stop[, step]) -> range object
# Exemplo utilizando a função built-in range
# Exibindo a tabuada do 8
for numero in range(0, 81, 8):
    print(numero, end=" ")
