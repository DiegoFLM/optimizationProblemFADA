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
    #time = 10
    #for i in range(10):
     #   lines.append('a')


    #SetOtherArrays
    bestA = [''] * (n-1)
    bestB = [''] * (n-1)

    timeBestA = [float('inf')] * n
    timeBestB = [float('inf')] * n

    timeBestA[n-1] = a[n-1]
    timeBestB[n-1] = b[n-1]

    bestWayBeginning = ''
    bestWay = [''] * n



    #DetermineBestStartingPoint

    for i in range (n-2, -1, -1):
        #Determine the best way from a[i]
        if (timeBestA[i+1] < ab[i] + timeBestB[i+1]):
            bestA[i] = 'a'
            timeBestA[i] = a[i] + timeBestA[i+1]
        else:
            bestA[i] = 'b'
            timeBestA[i] = a[i] + ab[i] + timeBestB[i+1]

        #Determine the best way from b[i]
        if (timeBestB[i+1] <= ba[i] + timeBestA[i+1]):
            bestB[i] = 'b'
            timeBestB[i] = b[i] + timeBestB[i+1]
        else:
            bestB[i] = 'a'
            timeBestB[i] = b[i] + ba[i] + timeBestA[i+1]


    #Specify the best way
    if (timeBestA[0] < timeBestB[0]):
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
            if (bestA[j-1] == 'a'):
                bestWay[j] = 'a'
                bestTime += a[j]
            else:
                bestWay[j] = 'b'
                bestTime += ab[j-1] + b[j] 
        else:
            if (bestB[j-1] == 'a'):
                bestWay[j] = 'a'
                bestTime += ba[j-1] + a[j]
            else:
                bestWay[j] = 'b'
                bestTime += b[j]


    print("bestWay = " + str(bestWay))
    print("bestA = " + str(bestA))
    print("bestB = " + str(bestB))
    print("a = " + str(a))
    print("ab = " + str(ab))
    print("ba = " + str(ba))
    print("b = " + str(b))
    print("bestTime = " + str(bestTime))
    print("timeBestA = " + str(timeBestA))
    print("timeBestB = " + str(timeBestB))


    time = bestTime
    lines = bestWay
    # Fin del algoritmo

    # Salida del algoritmo (No modificar)
    return n, time, lines


def main():
    n, a, b, ab, ba = input()
    res = solve(n, a, b, ab, ba)
    output(res)
    


if __name__ == "__main__":
    main()
