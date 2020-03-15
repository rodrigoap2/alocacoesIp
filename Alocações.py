import heapq
import random
from Aula import Aula
from Monitor import Monitor
from Combinacao import Combinacao

conjuntoAulas = []
conjuntoMonitores = []
qtdeMonitoress = 0
x = 0

#Primeiro adicionar as aulas, depois adicionar os monitores, depois fazer a distribuição
def gerarCombinacao():
    combinacao = Combinacao(x*4/qtdeMonitoress)
    for aula in conjuntoAulas:
        while aula.qtdeMonitores() < 4:
            monitor = conjuntoMonitores[random.randint(0,qtdeMonitoress-1)]
            if aula.tipo in monitor.disponibilidade and monitor not in aula.monitores:
                monitor.aulas.append(aula.dia)
                monitor.qtdeAlocacoes += 1
                aula.monitores.append(monitor)
        newAula = Aula(aula.dia,aula.tipo)
        newAula.setMonitores(aula.monitores)
        combinacao.addAula(newAula)
        aula.resetMonitores()
    for monitor in conjuntoMonitores:
        monitor.resetAulas()
    return combinacao

x = int(input("Digite a quantidade de aulas"))
for i in range(0,x):
    dataAula = input("Digite a data da aula")
    tipoAula = input("Digite o tipo da aula")
    aula = Aula(dataAula,tipoAula)
    conjuntoAulas.append(aula)

qtdeMonitoress = int(input("Digite a quantidade de monitores"))
for i in range(0,qtdeMonitoress):
    nomeMonitor = input("Digite o nome do monitor")
    disponibilidadeMonitor = input("Digite entre espaços o tipo de dia disponível").split(' ')
    monitor = Monitor(nomeMonitor,disponibilidadeMonitor)
    conjuntoMonitores.append(monitor)
#Inicializando a população
for i in range(0,30):
    a = gerarCombinacao()
    a.calcularFitness()
    print(a.fitness)
#print(a.aulas)
#print(conjuntoAulas)
