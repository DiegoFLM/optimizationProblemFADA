nombreLectura = "in"
nombreEscritura = "out"

'''
input()
Función para leer el archivo bajo el formato establecido en el proyecto. El
nombre se cambia en la variable global "nombreLectura". (No modificar)
'''


def input():
    with open(nombreLectura+".txt", "r") as f:
        content = f.read().split('\n')
        n = int(content[0])
        a = list(map(lambda x: int(x), content[1].split(" ")))
        b = list(map(lambda x: int(x), content[2].split(" ")))
        ab = list(map(lambda x: int(x), content[3].split(" ")))
        ba = list(map(lambda x: int(x), content[4].split(" ")))
        return n, a, b, ab, ba


'''
output()
Función para escribir sobre el archivo según lo solicitado en el proyecto. El
nombre del archivo se cambia en la variable global "nombreEscritura". (No modificar método)
'''


def output(output):
    n, time, lines = output
    toWrite = ""
    toWrite += str(n) + "\n"
    toWrite += str(time)
    for line in lines:
        toWrite += "\n" + str(line)

    with open(nombreEscritura+".txt", "w") as f:
        f.write(toWrite)


'''
Función donde deben introducir la lógica de su algoritmo. Pueden declarar
variables globales si lo consideran conveniente.
'''


def solve(n, a, b, ab, ba):
    # Declaración de variables para la salida del algoritmo (No modificar)
    time = 0
    lines = []

    # Algoritmo
    
    #SetArrays&Matrices
    bestChoiceMatrix = [['z'] * (n-1), ['z'] * (n-1)]

    bestTimeMatrix = [[float('inf')] * n, [float('inf')] * n]

    bestTimeMatrix[0][n-1] = a[n-1]
    bestTimeMatrix[1][n-1] = b[n-1]

    bestWayBeginning = ''
    bestWay = [''] * n

    #DetermineBestChoices&BestTimes
    for i in range (n-2, -1, -1):
        #Determine the best way from a[i]
        if (bestTimeMatrix[0][i+1] < ab[i] + bestTimeMatrix[1][i+1]):
            bestChoiceMatrix[0][i] = 'a'
            bestTimeMatrix[0][i] = a[i] + bestTimeMatrix[0][i+1]
        else:
            bestChoiceMatrix[0][i] = 'b'
            bestTimeMatrix[0][i] = a[i] + ab[i] + bestTimeMatrix[1][i+1]

        #Determine the best way from b[i]
        if (bestTimeMatrix[1][i+1] < ba[i] + bestTimeMatrix[0][i+1]):
            bestChoiceMatrix[1][i] = 'b'
            bestTimeMatrix[1][i] = b[i] + bestTimeMatrix[1][i+1]
        else:
            bestChoiceMatrix[1][i] = 'a'
            bestTimeMatrix[1][i] = b[i] + ba[i] + bestTimeMatrix[0][i+1]

    #Specify the best way
    if (bestTimeMatrix[0][0] < bestTimeMatrix[1][0]):
      bestWayBeginning = 'A'
    else:
      bestWayBeginning = 'B'


    #ObtainingBestWay&Time
    bestTime = 0

    if (bestWayBeginning == 'A'):
        bestWay[0] = 'a'
        bestTime += a[0]
    elif (bestWayBeginning == 'B'):
        bestWay[0] = 'b'
        bestTime += b[0]
    else:
        print('Error in bestWay[0]')

    for j in range(1, n):
        if (bestWay[j-1] == 'a'):
            if (bestChoiceMatrix[0][j-1] == 'a'):
                bestWay[j] = 'a'
                bestTime += a[j]
            else:
                bestWay[j] = 'b'
                bestTime += ab[j-1] + b[j] 
        else:
            if (bestChoiceMatrix[1][j-1] == 'a'):
                bestWay[j] = 'a'
                bestTime += ba[j-1] + a[j]
            else:
                bestWay[j] = 'b'
                bestTime += b[j]

    time = bestTime
    lines = bestWay
    # Fin del algoritmo

    # Salida del algoritmo (No modificar)
    return n, time, lines



import random as rd
def testGenerator(n):

    a = [float('inf')] * n
    b = [float('inf')] * n
    ab = [float('inf')] * ( n - 1 )
    ba = [float('inf')] * ( n - 1 )

    for j in range ( n - 1 ):
        a[j] = rd.randint(1, 10 * n)
        b[j] = rd.randint(1, 10 * n)
        ab[j] = rd.randint(1, 10 * n)
        ba[j] = rd.randint(1, 10 * n)
        a[n - 1] = rd.randint(1, 10 * n)
        b[n - 1] = rd.randint(1, 10 * n)
    return n, a, b, ab, ba


import time

def main():
    #n, a, b, ab, ba = input()
    #res = solve(n, a, b, ab, ba)
    #output(res)
    
    for i in range (1, 15000, 37):
        inicio = time.time()
        y = testGenerator(i)
        salida = [0 for i in range(y[0])]
        solve(y[0], y[1], y[2], y[3], y[4])
        fin = time.time()
        print(str(i) + " " + str(fin-inicio))


if __name__ == "__main__":
    main()
