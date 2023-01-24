import pandas as pd

def poblacion():
    df = pd.read_csv('List of cities proper by population density11.csv')
    ciudades = pd.DataFrame(df, columns=["City", "Population"])
    print(ciudades.head(10))



def KM2():
    df = pd.read_csv('List of cities proper by population density11.csv')
    ciudades = pd.DataFrame(df, columns=["City", "Area KM2"])
    print( ciudades.head(10))


def M2():
    df = pd.read_csv('List of cities proper by population density11.csv')
    ciudades = pd.DataFrame(df, columns=["City", "Area   M2"])
    print( ciudades.head(10))