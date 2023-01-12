import matplotlib.pyplot as plt

import funciones


def graficar():
    contador =0
    list = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    imprimir = []
    while contador < len(list):
        imprimir.append(funciones.mostrarBattery(list[contador]))
        contador = contador + 1

    plt.hist(imprimir)
    plt.xlabel('baterias')
    plt.show()




graficar()
