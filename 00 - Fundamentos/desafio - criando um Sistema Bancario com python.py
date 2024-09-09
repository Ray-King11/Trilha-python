import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            self._index += 1
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
    
class PessoaFisica:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

class Historico:
    def __init__(self):
        self.movimentacoes = []

    def adicionar_movimentacao(self, tipo, valor):
        self.movimentacoes.append({"tipo": tipo, "valor": valor})

    def gerar_relatorio(self):
        return self.movimentacoes

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

class ContaBancariaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.numero_saques = 0
        self.limite_saques = limite_saques

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_movimentacao("Depósito", valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > 0:
            if valor > self._saldo:
                print("Saldo insuficiente!")
                return False
            
            if valor > self.limite:
                print("O valor do saque excede o limite.")
                return False
            
            if self.numero_saques >= self.limite_saques:
                print("Número máximo de saques excedido.")
                return False

            self._saldo -= valor
            self._historico.adicionar_movimentacao("Saque", valor)
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def consultar_extrato(self):
        print("\n================ EXTRATO ================")
        extrato = ""
        movimentacoes = self._historico.gerar_relatorio()
        if not movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            for mov in movimentacoes:
                extrato += f"\n{mov['tipo']}:\n\tR$ {mov['valor']:.2f}\n"

        print(extrato)
        print(f"\nSaldo: R$ {self._saldo:.2f}")
        print("==========================================")

    @staticmethod
    def criar_cliente(clientes):
        cpf = input("Informe o CPF (somente números): ")
        if any(cliente.cpf == cpf for cliente in clientes):
            print("Já existe cliente com esse CPF!")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        clientes.append(cliente)
        print("Cliente criado com sucesso!")

    @staticmethod
    def criar_conta(numero_conta, cliente, contas):
        conta = ContaBancariaCorrente(numero=numero_conta, cliente=cliente)
        contas.append(conta)
        cliente.contas.append(conta)
        print("Conta criada com sucesso!")

    @staticmethod
    def listar_contas(contas):
        if not contas:
            print("Nenhuma conta encontrada.")
            return
        for conta in ContasIterador(contas):
            print("=" * 100)
            print(textwrap.dedent(str(conta)))

def main():
    menu = """
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Nova Conta
    [4] Listar Contas
    [5] Novo Usuário
    [6] Sair

    => """

    clientes = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "0":
            valor = float(input("Informe o valor do depósito: "))
            if contas:
                conta = contas[0]  # Supondo que vamos operar na primeira conta
                conta.depositar(valor)
            else:
                print("Nenhuma conta encontrada.")

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            if contas:
                conta = contas[0]  # Supondo que vamos operar na primeira conta
                conta.sacar(valor)
            else:
                print("Nenhuma conta encontrada.")

        elif opcao == "2":
            if contas:
                conta = contas[0]  # Supondo que vamos operar na primeira conta
                conta.consultar_extrato()
            else:
                print("Nenhuma conta encontrada.")

        elif opcao == "3":
            numero_conta = input("Informe o número da nova conta: ")
            if clientes:
                cliente = clientes[0]  # Supondo que vamos criar a conta para o primeiro cliente
                ContaBancariaCorrente.criar_conta(numero_conta, cliente, contas)
            else:
                print("Nenhum cliente encontrado.")

        elif opcao == "4":
            ContaBancariaCorrente.listar_contas(contas)

        elif opcao == "5":
            ContaBancariaCorrente.criar_cliente(clientes)

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()

