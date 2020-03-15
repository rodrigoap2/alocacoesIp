import heapq
from Aula import Aula
from Monitor import Monitor

conjuntoAulas = []
conjuntoMonitores = []
qtdeMonitoress = 0
#Primeiro adicionar as aulas, depois adicionar os monitores, depois fazer a distribuição
def designarMonitores():
    heapq.heapify(conjuntoMonitores)
    for aula in conjuntoAulas:
        media = calcularMedia()
        print(conjuntoMonitores)
        contador = 0
        while contador < (len(conjuntoMonitores)*2):
            monitor = heapq.heappop(conjuntoMonitores)
            monitor.visitado += 1
            if aula.qtdeMonitores() >= 4:
                heapq.heappush(conjuntoMonitores, monitor)
                break
            if aula.tipo in monitor.disponibilidade and monitor.nome not in aula.monitores and (monitor.qtdeAulas() <= media or contador > len(conjuntoMonitores)/2 or aula.tipo == 1 or aula.tipo == 4):
                monitor.aulas.append(aula.dia)
                monitor.qtdeAlocacoes += 1
                aula.monitores.append(monitor.nome)
            heapq.heappush(conjuntoMonitores,monitor)
            contador+=1
        print(aula)

def calcularMedia():
    valor = 0
    for monitor in conjuntoMonitores:
        valor += monitor.qtdeAulas()
    return valor/qtdeMonitoress

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
designarMonitores()
#print(conjuntoAulas)
for monitor in conjuntoMonitores:
    stri = ""
    for aula in monitor.aulas:
        stri += aula
    print(monitor.nome + " " + str(monitor.qtdeAulas()) + " " + stri)
