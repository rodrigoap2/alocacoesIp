class Aula:
    def __init__(self,dia,tipo):
        self.dia = dia
        self.tipo = tipo
        self.monitores = []

    def addMonitor(self,monitor):
        self.monitores.append(monitor)

    def qtdeMonitores(self):
        return len(self.monitores)

    def __str__(self):
        str = ""
        for monitor in self.monitores:
            str += monitor + " "
        return self.dia + " " + "{" + str + "}"

    def __repr__(self):
        return str(self)