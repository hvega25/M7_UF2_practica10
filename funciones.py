import pandas as pd

def mostrarXid(ID):

    df = pd.read_csv('test.csv')
    df_mask = df['id'] == ID
    filtered_df = df[df_mask]
    print(filtered_df['clock_speed'])

def mostrarPixe(ID):

    df = pd.read_csv('test.csv')
    df_mask = df['id'] == ID
    filtered_df = df[df_mask]
    return filtered_df['px_width']


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


