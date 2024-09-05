class ContaBancaria:
    def __init__(self, numero, titular, limite=500, limite_saques=3):
        self.numero = numero
        self.titular = titular
        self.saldo = 0
        self.limite = limite
        self.extrato = ""
        self.numero_saques = 0
        self.limite_saques = limite_saques

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > 0:
            if valor > self.saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > self.limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif self.numero_saques >= self.limite_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            else:
                self.saldo -= valor
                self.extrato += f"Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def consultar_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

def main():
    menu = """
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair

    => """

    conta = ContaBancaria(numero=12345, titular="João Silva")

    while True:
        opcao = input(menu)

        if opcao == "0":
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        elif opcao == "2":
            conta.consultar_extrato()

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
