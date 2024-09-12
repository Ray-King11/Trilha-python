class Cachorro:
    def fazer_som(self):
        return "Au au!"

class Gato:
    def fazer_som(self):
        return "Miau!"
    
def imprmir_som(animal):
    print(animal.fazer_som())

# Criando objetos
cachorro = Cachorro()
gato = Gato()

# Chamando o mesmo método para objetos diferentes
imprmir_som(cachorro)
imprmir_som(gato)
