import heapq
import random
from Aula import Aula
from Monitor import Monitor
from Combinacao import Combinacao

conjuntoAulas = []
conjuntoMonitores = []
qtdeMonitoress = 0
x = 0


def alocarMonitores(aula):
    while aula.qtdeMonitores() < 4:
        monitor = conjuntoMonitores[random.randint(0, qtdeMonitoress - 1)]
        if aula.tipo in monitor.disponibilidade and monitor not in aula.monitores:
            monitor.aulas.append(aula.dia)
            monitor.qtdeAlocacoes += 1
            aula.monitores.append(monitor)
    return aula

#Primeiro adicionar as aulas, depois adicionar os monitores, depois fazer a distribuição
def gerarCombinacao():
    combinacao = Combinacao(x*4/qtdeMonitoress)
    for aula in conjuntoAulas:
        aula = alocarMonitores(aula)
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
populacao = []
qtdeInicio = 30
for i in range(0,qtdeInicio):
    combinacao = gerarCombinacao()
    combinacao.calcularFitness()
    populacao.append(combinacao)
populacao.sort(reverse = True)
contador = 0
print(populacao[0].fitness)
while contador < 300000 and populacao[0].fitness > 200:
    contador += 1
    pai1 = populacao[random.randint(0, 4)]
    pai2 = populacao[random.randint(0, 4)]
    filho = Combinacao(x*4/qtdeMonitoress)
    qtdePai1 = random.randint(0, x)
    for aula in pai1.getAulasIntervalo(0,qtdePai1):
        filho.addAula(aula)
    for aula in pai2.getAulasIntervalo(qtdePai1,x):
        filho.addAula(aula)
    filho.calcularFitness()
    populacao[qtdeInicio-1] = filho
    populacao.sort(reverse = True)
print(populacao[0].fitness)
for aula in populacao[0].aulas:
    print(aula.dia)
    print(aula.monitores)
print('gg')
