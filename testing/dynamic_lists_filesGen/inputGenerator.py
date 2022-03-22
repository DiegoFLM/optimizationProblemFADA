#nombreLectura = "in"
#nombreEscritura = "out"

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


def output(output, nombreEscritura):
    #n, time, lines = output
    n, a, b, ab, ba = output
    toWrite = ""
    toWrite += str(n) + "\n"
    #toWrite += str(time)
    #for line in a:
        #toWrite += "\n" + str(line)


    for num in range (n - 1):
        toWrite += str(a[num]) + " "
    toWrite += str(a[n-1]) + "\n"

    for num in range (n - 1):
        toWrite += str(b[num]) + " "
    toWrite += str(b[n-1]) + "\n"

    for num in range (n - 2):
        toWrite += str(ab[num]) + " "
    toWrite += str(ab[n-2]) + "\n"

    for num in range (n - 2):
        toWrite += str(ba[num]) + " "
    toWrite += str(ba[n-2]) + "\n"

    #toWrite += str(a) + "\n" 
    #toWrite += str(b) + "\n"
    #toWrite += str(ab) + "\n"
    #toWrite += str(ba)

    with open(nombreEscritura+".txt", "w") as f:
        f.write(toWrite)


'''
Función donde deben introducir la lógica de su algoritmo. Pueden declarar
variables globales si lo consideran conveniente.
'''


def generate(n):
    # Declaración de variables para la salida del algoritmo (No modificar)
    #time = 0
    #lines = []

    # Algoritmo
    import random as rd

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
    
    # Fin del algoritmo

    # Salida del algoritmo (No modificar)
    return n, a, b, ab, ba



def main():
    #n, a, b, ab, ba = input()
    #res = generate(n)
    #output(res)
    

    #for i in range(1, 1500, 37):
    for i in range(5, 15):
        res = generate(i)
        nombreEscritura = str(i) 
        output(res, nombreEscritura)
        print(res)
    




if __name__ == "__main__":
    main()
