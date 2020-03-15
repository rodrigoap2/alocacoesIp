class Combinacao:
    def __init__(self, media):
        self.aulas = []
        self.fitness = 0
        # Media é a soma da quantidade de aulas dos monitores/qtdeMonitores, que pode ser resumido a qtdeAulas*qtdeMonitoresPorAula/qtdeMontores
        self.media = media

    def getCombinacao(self):
        return self.aulas

    def addAula(self,aula):
        self.aulas.append(aula)

    def getAulasIntervalo(self,inicio,fim):
        aulas = []
        for i in range(inicio,fim):
            aulas.append(self.aulas[i])
        return aulas

    def calcularFitness(self):
        monitores = set()
        for aula in self.aulas:
            for monitor in aula.monitores:
                monitores.add(monitor)
        for monitor in monitores:
            self.fitness += (int(monitor.qtdeAulas())-self.media)*(int(monitor.qtdeAulas())-self.media)
        self.fitness /= len(monitores)/100
        self.fitness = int(self.fitness)

    def __str__(self):
        return str(self.fitness)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
       return self.fitness > other.fitness