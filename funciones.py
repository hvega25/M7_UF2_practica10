import pandas as pd #importa la libreria para leer el csv

def mostrarClockSpeed(ID):#funcion que retorna la velocidad de procesador

    df = pd.read_csv('test.csv') #lee un archivo csv y lo guarda en una variable
    df_mask = df['id'] == ID #compara si el valor de la columna id de la tabla es igual al valor de parametro y lo guarda
    filtered_df = df[df_mask] # guarda el valor encontrado en una variable
    return filtered_df['clock_speed'] #retorno el valor

def mostrarPixe(ID):

    df = pd.read_csv('test.csv')
    df_mask = df['id'] == ID
    filtered_df = df[df_mask]
    return filtered_df['px_width']


def mostrarBattery(ID):

    df = pd.read_csv('test.csv')
    df_mask = df['id'] == ID
    filtered_df = df[df_mask]
    return filtered_df['battery_power']


