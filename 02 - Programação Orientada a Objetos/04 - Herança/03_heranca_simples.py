class Smartphone:
    def __init__(self, cor, marca, armazenamento, preco):
        self.cor = cor
        self.marca = marca
        self.armazenamento = armazenamento  
        self.preco = preco
    
    def ligar_smartphone(self):
        print("Ligando o Smartphone")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Apple(Smartphone):
    pass

class Samsung(Smartphone):
    pass

class Moto(Smartphone):
    def __init__(self, cor, marca, armazenamento, preco, carregado):
        super().__init__(cor, marca, armazenamento, preco)
        self.carregado = carregado
    
    def esta_carregando(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

# Instanciando objetos com valores corrigidos
iPhone_15_pro_max = Apple("dourado", "apple", 512, 8.999)
galaxy_s24_ultra = Samsung("verde", "samsung", 512, 9.890)
motorola_edge_50_ultra_5g = Moto("madeira", "moto", 512, 4.999, True)  

# Imprimindo informações dos objetos
print(iPhone_15_pro_max)
print(galaxy_s24_ultra)
print(motorola_edge_50_ultra_5g)


