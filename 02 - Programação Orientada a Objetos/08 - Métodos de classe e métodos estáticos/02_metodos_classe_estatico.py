class Calculadora:
    fator = 1.2  # Variável de classe

    def __init__(self, valor):
        self.valor = valor  # Variável de instância

    @classmethod
    def alterar_fator(cls, novo_fator):
        if novo_fator > 0:
            cls.fator = novo_fator  # Altera a variável de classe
        else:
            raise ValueError("O fator deve ser um número positivo.")

    @staticmethod
    def somar(a, b):
        return a + b  # Método estático, sem acesso à classe ou instância

    def aplicar_fator(self):
        return self.valor * self.fator  # Usa o fator (variável de classe)

# Exemplo de uso

# Chamando o método estático sem criar uma instância
resultado = Calculadora.somar(10, 5)
print(f"Resultado da soma estática: {resultado}")

# Criando uma instância da Calculadora
calc = Calculadora(100)
print(f"Valor com fator inicial: {calc.aplicar_fator()}")

# Alterando o fator com o classmethod
Calculadora.alterar_fator(1.5)
print(f"Valor após alterar o fator: {calc.aplicar_fator()}")
