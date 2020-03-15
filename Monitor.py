class Monitor:
    def __init__(self,nome,disponibilidade):
        self.nome = nome
        self.disponibilidade = disponibilidade
        self.aulas = []
        self.qtdeAlocacoes = 0

    def addAula(self,diaAula):
        self.aulas.append(diaAula)

    def qtdeAulas(self):
        return len(self.aulas)

    def resetAulas(self):
        self.aulas = []
        self.qtdeAlocacoes = 0

    def setAulas(self, aulas, qtde):
        self.aulas = aulas
        self.qtdeAlocacoes = qtde

    def __str__(self):
        return self.nome

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return ((self.qtdeAlocacoes*5)+self.visitado)  < ((other.qtdeAlocacoes*5) + other.visitado)