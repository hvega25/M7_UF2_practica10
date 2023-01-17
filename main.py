
import matplotlib.pyplot as plt
import funciones


def graficar_bateria():
    contador =0
    contador1=0
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    imprimir = []

    while contador < len(list):
        imprimir.append(funciones.mostrarBattery(list[contador]))
        contador = contador + 1


    while contador1 < len(list):
        plt.bar(contador1 , imprimir[contador1])

    plt.xlabel('Indice')
    plt.ylabel('mhz')
    plt.show()


def graficar_clockSpeed():
    contador =0
    contador1=0
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    imprimir = []

    while contador < len(list):
        imprimir.append(funciones.mostrarXid(list[contador]))
        contador = contador + 1


    while contador1 < len(list):
        plt.bar(contador1 , imprimir[contador1])

    plt.xlabel('Indice')
    plt.ylabel('Clock speed')
    plt.show()

def graficar_megaPixel():
    contador =0
    contador1=0
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    imprimir = []

    while contador < len(list):
        imprimir.append(funciones.mostrarPixe(list[contador]))
        contador = contador + 1


    while contador1 < len(list):
        plt.bar(contador1 , imprimir[contador1])

    plt.xlabel('Indice')
    plt.ylabel('Clock speed')
    plt.show()




graficar_bateria()
graficar_clockSpeed()
graficar_megaPixel()