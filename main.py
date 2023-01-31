import funciones
import matplotlib.pyplot as plt


def imprimir_poblacion():
    retorno = funciones.poblacion()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(retorno['Population'].astype(str).str.replace(',', '').astype(float),  labels=retorno['City'], autopct='%1.1f%%', startangle=90)
    plt.title('Poblacion')
    plt.legend()
    plt.show()

def imprimir_poblacion_KM2():
    retorno = funciones.KM2()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(retorno['Density KM2'].astype(str).str.replace(',', '').astype(float), labels=retorno['City'], autopct='%1.1f%%', startangle=90)
    plt.title('Densidad kM2')
    plt.legend()
    plt.show()

def imprimir_poblacion_M2():
    retorno = funciones.M2()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(retorno['Density  M2'].astype(str).str.replace(',', '').astype(float), labels=retorno['City'], autopct='%1.1f%%', startangle=90)
    plt.title('Densidad M2')
    plt.legend()
    plt.show()


imprimir_poblacion()
imprimir_poblacion_KM2()
imprimir_poblacion_M2()
