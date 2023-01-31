import pandas as pd

def poblacion():
    df = pd.read_csv('List of cities proper by population density11.csv')
    ciudades = pd.DataFrame(df, columns=["City", "Population"])
    retorno = ciudades.head(10)
    return retorno




def KM2():
    df = pd.read_csv('List of cities proper by population density11.csv')
    ciudades = pd.DataFrame(df, columns=["City", "Density KM2"])
    retorno = ciudades.head(10)
    return retorno


def M2():
    df = pd.read_csv('List of cities proper by population density11.csv')
    ciudades = pd.DataFrame(df, columns=["City", "Density  M2"])
    retorno = ciudades.head(10)
    return retorno
