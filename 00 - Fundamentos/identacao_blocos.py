def sacar(valor): # inicio do boco
    saldo = 500

    if saldo >= valor:  # inicio do bloco do if
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor

    if  saldo >= valor:
        print("Obrigado tenha um bom dia")
    

sacar(1000)

    # fim do bloco do if 
    
# fim do bloco do métodod