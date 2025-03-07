import math
import copy

#Asigno a ambos jugadores su id
maxId = int(input())
minId = 1 - maxId


#Creo clase carta que almacena el dueño, id y los movimientos. Cuando se crea una instancia de carta se creara una lista emparajando el movimiento en el eje x e y de cada accion de esa carta
class carta():
    def __init__(self, owner, card_id, dx_1, dy_1, dx_2, dy_2, dx_3, dy_3, dx_4, dy_4):
        self.owner = owner
        self.card_id = card_id
        self.dx_1 = dx_1
        self.dy_1 = dy_1
        self.dx_2 = dx_2
        self.dy_2 = dy_2
        self.dx_3 = dx_3
        self.dy_3 = dy_3
        self.dx_4 = dx_4
        self.dy_4 = dy_4
        self.listaMovimientos = self.movimientos()

    def movimientos(self):
        movimientos = []
        if not (self.dx_1 == 0 and self.dy_1 == 0):
            movimientos.append((self.dy_1, self.dx_1))#Almaceno primero y porque he considerado primero filas y luego columnas
        if not (self.dx_2 == 0 and self.dy_2 == 0):
            movimientos.append((self.dy_2, self.dx_2))
        if not (self.dx_3 == 0 and self.dy_3 == 0):
            movimientos.append((self.dy_3, self.dx_3))
        if not (self.dx_4 == 0 and self.dy_4 == 0):
            movimientos.append((self.dy_4, self.dx_4))
        return movimientos


#Funcion que calcula los movimientos posibles del jugador que se pase como parametro
def calcularMovimientos(idJugador, nodo, cartas):
    movimientosJugador = []
    piezas = []
    cartasJugador = []
    if idJugador == 0:
        for i in range(5):
            for j in range(5):
                if nodo[0][i][j] in ['w', 'W']:
                    piezas.append([i,j])#Almaceno las posiciones de las piezas en el nodo actual
        for i in cartas:
            if i.owner == 0:
                for j in i.listaMovimientos:
                    cartasJugador.append([j, i.card_id])#Almaceno la accion(movimiento eje x e y) junto a el id de la carta al que pertenece

        for i in piezas:
            for j in cartasJugador:
                if esPosible(i, j[0], idJugador, nodo):
                    movimientosJugador.append([i,j])#Almaceno la posicion de la pieza y accion
    else:
        for i in range(5):
            for j in range(5):
                if nodo[0][i][j] in ['b', 'B']:
                    piezas.append([i,j])
        for i in cartas:
            if i.owner == 1:
                for j in i.listaMovimientos:
                    cartasJugador.append([j, i.card_id])
        for i in piezas:
            for j in cartasJugador:
                if esPosible(i, j[0], idJugador, nodo):
                    movimientosJugador.append([i,j])
    return movimientosJugador


#Funcion que recibe la posiion de una pieza y una accion y indica si es posible, es decir, que no se salga del tablero o se posicione en la misma celda de una pieza de su equipo
def esPosible(posPieza, movimiento, idJugador, nodo):
    nuevaPosPieza = []
    posible = False
    if idJugador == 0:
        nuevaPosPieza = [posPieza[0] - movimiento[0] , posPieza[1] + movimiento[1]]
        if 0 <= nuevaPosPieza[0] <= 4 and 0 <= nuevaPosPieza[1] <= 4:
            if not (nodo[0][nuevaPosPieza[0]][nuevaPosPieza[1]] in ['w', 'W']):
                posible = True
    else:
        nuevaPosPieza = [posPieza[0] - movimiento[0] , posPieza[1] + movimiento[1]]
        if 0 <= nuevaPosPieza[0] <= 4 and 0 <= nuevaPosPieza[1] <= 4:
            if not (nodo[0][nuevaPosPieza[0]][nuevaPosPieza[1]] in ['b', 'B']):
                posible = True
    return posible


#Esta funcion analiza el nodo he indica si es final, es decir, si alguno de los jugadores ha ganado
def esFinal(nodo):
    W = False
    B = False
    if (nodo[0][2] == 'W') or (nodo[4][2] == 'B'):
        return True
    for i in range(5):
        for j in range(5):
            if nodo[i][j] == 'W':
                W = True
            if nodo[i][j] == 'B':
                B = True
    if W == False or B == False:
        return True
    else:
        return False


#Esta funcion recibe un movimiento el cual esta compuesto por la pieza que se quiere mover, la accion(posicion x e y) y el id de la carta, y lo convierte para que codeingame lo puede entender y aplicarlo
def convertirMovimiento(movimiento):
    letras = ['A', 'B', 'C', 'D', 'E']
    posPieza = movimiento[0]
    movimientoPieza = movimiento[1][0]
    nuevaPosPieza = [posPieza[0] - movimientoPieza[0] , posPieza[1] + movimientoPieza[1]]
    letraPosPieza = letras[movimiento[0][1]]
    numPosPieza = str(5 - movimiento[0][0])#Le resto 5 porque para code in game las posicones de filas va al reves que yo, de abajo a arriba
    letraNuevaPosPieza = letras[nuevaPosPieza[1]]
    numNuevaPosPieza= str(5 - nuevaPosPieza[0])
    accion = letraPosPieza + numPosPieza + letraNuevaPosPieza + numNuevaPosPieza
    return movimiento[1][1], str(accion)#Devuelvo el id de la carta, y la accion


#Esta funcion recibe un id y indica si es el de jugadorMax o no
def esJugadorMax(jugador):
    return maxId == jugador


#Esta funcion recibe un nodo y devuelve un valor en funcion si beneficia a jugadorMax o a jugadorMin
def evaluacionNodo(nodo):
    masterMax = False
    masterMin = False
    posMasterMax = [0 ,0]
    posMasterMin = [0, 0]
    if maxId == 0:
        for i in range(5):
            for j in range(5):
                if nodo[0][i][j] == 'W':
                    masterMax = True
                    posMasterMax = [i, j]
                if nodo[0][i][j] == 'B':
                    masterMin = True
                    posMasterMin = [i, j]
        if masterMin == False:
            return 5000
        if masterMax == False:
            return -5000
        if posMasterMax == [0, 2]:
            return 5000
        if posMasterMin == [4, 2]:
            return -5000
    else:
        for i in range(5):
            for j in range(5):
                if nodo[0][i][j] == 'B':
                    masterMax = True
                    posMasterMax = [i, j]
                if nodo[0][i][j] == 'W':
                    masterMin = True
                    posMasterMin = [i, j]
        if masterMin == False:
            return 5000
        if masterMax == False:
            return -5000
        if posMasterMax == [4, 2]:
            return 5000
        if posMasterMin == [0, 2]:
            return -5000

    if maxId == 0:
        puntuacionesCasillas = [

            [-100, -100, -100, -100, -100],
            [ -50, -50,-50, -50, -50],
            [200, 300, 300, 300, 200],
            [100, 200, 200, 200, 100],
            [-10, -10, -10, -10, -10]

        ]
        posPiezas = []
        for i in range(len(nodo[0])):
            for j in range(len(nodo[0][i])):
                if nodo[0][i][j] == 'w' or nodo[0][i][j] == 'W':
                    posPiezas.append((i, j))
    else:
        puntuacionesCasillas = [

            [-10, -10, -10, -10, -10],
            [100, 200, 200, 200, 100],
            [ 200, 300, 300, 300, 200],
            [ -50,  -50, -50, -50, -50],
            [-100, -100, -100, -100, -100]

        ]
        posPiezas = []
        for i in range(len(nodo[0])):
            for j in range(len(nodo[0][i])):
                if nodo[0][i][j] == 'b' or nodo[0][i][j] == 'B':
                    posPiezas.append((i, j))
    suma = 0
    for pos in posPiezas:
        suma += puntuacionesCasillas[pos[0]][pos[1]]
    if maxId == 0:
        if nodo[1][0] > nodo[1][1]:
            return 2000 + suma
        elif nodo[1][0] < nodo[1][1]:
            return -2000 - suma
        elif nodo[1][0] == 1 and  nodo[1][1] == 1:
            return 1000 + suma
        else:
            return suma
    elif maxId == 1:
        if nodo[1][1] > nodo[1][0]:
            return 2000 + suma
        elif nodo[1][1] < nodo[1][0]:
            return -2000 - suma
        elif nodo[1][0] == 1 and  nodo[1][1] == 1:
            return 1000 + suma
        else:
            return suma
    return


#Esta funcion aplica una accion a una copia de la matriz que utilizamos como tablero. Ademas almacena en el nodo si alguno de los jugadores ha eliminadao una pieza del rival
def aplica(nodo, movimiento, idJugador):
    nuevoNodo = copy.deepcopy(nodo)
    posPieza = movimiento[0]
    movimientoPieza = movimiento[1][0]
    if idJugador == 0:
        nuevaPosPieza = [posPieza[0] - movimientoPieza[0] , posPieza[1] + movimientoPieza[1]]
        if nodo[0][nuevaPosPieza[0]][nuevaPosPieza[1]] in ['b', 'B']:
            nuevoNodo[1][0] = 1
    else:
         nuevaPosPieza = [posPieza[0] - movimientoPieza[0] , posPieza[1] + movimientoPieza[1]]
         if nodo[0][nuevaPosPieza[0]][nuevaPosPieza[1]] in ['w', 'W']:
            nuevoNodo[1][1] = 1
    aux = nuevoNodo[0][posPieza[0]][posPieza[1]]
    nuevoNodo[0][posPieza[0]][posPieza[1]] = '.'
    nuevoNodo[0][nuevaPosPieza[0]][nuevaPosPieza[1]] = aux
    return nuevoNodo


#Implementacion del algoritmo MiniMax
def alfa_beta(nodo, profundidad, alfa, beta, esJugadorMax, cartas):#Solo puede mirar para profundidad 1 es decir un moviento mio y el que cre que hara el contrincate por eso cambiar evaluacion nodo
    if profundidad == 0 or esFinal(nodo[0]):
        return evaluacionNodo(nodo), None
    if esJugadorMax == True:
        value = -math.inf
        MejorMov = None
        movimientos = calcularMovimientos(maxId, nodo, cartas)
        for movimiento in movimientos:
            nuevoNodo = aplica(nodo, movimiento, maxId)
            valNuevoNodo, _ = alfa_beta(nuevoNodo, profundidad, alfa, beta, False, cartas)
            if valNuevoNodo > value:
                value = valNuevoNodo
                MejorMov = movimiento
                alfa = value
            if alfa >= beta:
                break
        return (value, MejorMov)
    else:
        value = math.inf
        MejorMov = None
        movimientos = calcularMovimientos(minId, nodo, cartas)
        for movimiento in movimientos:
            nuevoNodo = aplica(nodo, movimiento, minId)
            valNuevoNodo, _ = alfa_beta(nuevoNodo, profundidad-1, alfa, beta, True, cartas)
            if valNuevoNodo < value:
                value = valNuevoNodo
                MejorMov = movimiento
                beta = value
            if alfa >= beta:
                break
        return (value, MejorMov)


while True:
    nodo = [[], [0, 0]]#En nodo[0] guardo el tablero y en nodo[1] las piezas comidas --> nodo[1][0] piezas comidas por el id 0  y nodo[1][1] piezas comidas por el id 1
    movimientos = []
    cartas = []
    for i in range(5):#Matriz que utilizare como tablero
        row = input()
        nodo[0].append(list(row))
    for i in range(5):#Leeo, creo los objetos carta y los almaceno
        owner, card_id, dx_1, dy_1, dx_2, dy_2, dx_3, dy_3, dx_4, dy_4 = [int(j) for j in input().split()]
        nuevaCarta = carta(owner, card_id, dx_1, dy_1, dx_2, dy_2, dx_3, dy_3, dx_4, dy_4 )
        cartas.append(nuevaCarta)

    # Me salto los inputs que no quiero leer
    action_count = int(input())
    for i in range(action_count):
        inputs = input().split()

    mejorValor, mejorMovimiento = alfa_beta(nodo, 1, -math.inf, math.inf, True, cartas)

    idCarta, movimiento = convertirMovimiento(mejorMovimiento)#Convierto el movimiento obtenido por el algoritmo minimax en una accion que codeingame entienda

    print(idCarta, movimiento)
