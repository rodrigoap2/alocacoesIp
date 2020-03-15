from Monitor import Monitor
class Aula:
    def __init__(self,dia,tipo):
        self.dia = dia
        self.tipo = tipo
        self.monitores = []

    def addMonitor(self,monitor):
        self.monitores.append(monitor)

    def qtdeMonitores(self):
        return len(self.monitores)

    def resetMonitores(self):
        self.monitores = []

    def setMonitores(self,monitores):
        for monitor in monitores:
            monitorTemp = Monitor(monitor.nome,monitor.disponibilidade)
            monitorTemp.setAulas(monitor.aulas,monitor.qtdeAlocacoes)
            self.monitores.append(monitorTemp)

    def __str__(self):
        str = ""
        for monitor in self.monitores:
            str += monitor + " "
        return self.dia + " " + "{" + str + "}"

    def __repr__(self):
        return str(self)