class Family:
    def __init__(self, nome, mes_atual, ano_nascimento):
        self.nome = nome
        self.mes_atual = mes_atual
        self.ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self.ano_nascimento
        
    

pessoa = Family("Rildo Dugo Da Silva", 1969)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

pessoa = Family("Maria Aparecida Amorim Dugo Da Silva", 1972)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

pessoa = Family("Raí Amorim Dugo Da Silva", 2000)
print(F"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

pessoa = Family("Renan Amorim Dugo Da Silva", 2000)
print(F"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")