# Exemplo 1
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")


# Exemplo 2
saldo = 1848.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque")

if saldo <= saque:
    print("Saldo insuficiente")


# Exemplo 3 
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia pra o saque: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato...")

else:
    print("Opção inválida")
