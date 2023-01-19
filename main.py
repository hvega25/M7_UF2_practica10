import matplotlib.pyplot as plt #libreria para imprimir un grafico
import funciones #importa la hoja de funciones


def graficar_bateria(): #funcion que grafica
    contador =0 #primer contador que se usa para invocar a la funcion
    contador1=0 #segundo contador que se usa para la grafica
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]  # lista de los valores a buscar
    imprimir = [] #arreglo donde se guardan las valores que retorna

    while contador < len(list): #primer bucle que guarda en una variable lo que se ha invocado en las funciones
        imprimir.append(funciones.mostrarBattery(list[contador]))
        contador = contador + 1


    while contador1 < len(list):
        plt.bar(contador1 , imprimir[contador1])
        contador1 = contador1 + 1

    plt.xlabel('Indice')
    plt.ylabel('mAh')
    plt.show()


def graficar_MEGAPIXEL():
    contador =0
    contador1=0
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    imprimir = []

    while contador < len(list):
        imprimir.append(funciones.mostrarPixe(list[contador]))
        contador = contador + 1


    while contador1 < len(list):
        plt.bar(contador1 , imprimir[contador1])
        contador1 = contador1 + 1

    plt.xlabel('Indice')
    plt.ylabel('MEGAPIXEL')
    plt.show()


def graficar_MHZ():
    contador =0
    contador1=0
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    imprimir = []

    while contador < len(list):
        imprimir.append(funciones.mostrarClockSpeed(list[contador]))
        contador = contador + 1


    while contador1 < len(list):
        plt.bar(contador1 , imprimir[contador1])
        contador1 = contador1 + 1

    plt.xlabel('Indice')
    plt.ylabel('mhz')
    plt.show()


graficar_bateria()
graficar_MEGAPIXEL()
graficar_MHZ()