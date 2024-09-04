# Interposição de Variáveis %, format e f-string.
# Old style.
nome = "Ray"
idade = 23
profissao = "Progamador e Desenvolmimento de Software"
linguagem = "Python"
saldo = 185.435

dados = {"nome": "Ray", "idade": 23}

# % 
print("Nome: %s Idade: %d" % (nome, idade))


# format
print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

# f-string
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")

# Formatar string com f-string
PI = 3.141559

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

# Exemplos completos com format
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissão} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissão=profissao, linguagem=linguagem))
