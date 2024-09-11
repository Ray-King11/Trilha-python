class Passaro:
    def __init__(self, cor_penas):
        self.cor_penas = cor_penas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Calopsita(Passaro):
    def __init__(self, cor_penas, domestico):
        super().__init__(cor_penas)
        self.domestico = domestico


class Papagaio(Passaro):
    def __init__(self, cor_penas, cor_bico):
        super().__init__(cor_penas)
        self.cor_bico = cor_bico


class Selvagem:
    def __init__(self, cor_plumagem):
        self.cor_plumagem = cor_plumagem


class Rigs_Necks(Passaro, Selvagem):
    def __init__(self, cor_penas, cor_plumagem):
        Passaro.__init__(self, cor_penas)
        Selvagem.__init__(self, cor_plumagem)


class Argapones(Passaro, Selvagem):
    def __init__(self, cor_penas, cor_bico, cor_plumagem, domestico):
        Passaro.__init__(self, cor_penas)
        Selvagem.__init__(self, cor_plumagem)
        self.cor_bico = cor_bico
        self.domestico = domestico


# Criando objetos
rigs_necks = Rigs_Necks(cor_penas="zul", cor_plumagem="branco")
print(rigs_necks)

argapones = Argapones(cor_penas="zul", cor_bico="laranja", cor_plumagem="verde", domestico="não")
print(argapones)
