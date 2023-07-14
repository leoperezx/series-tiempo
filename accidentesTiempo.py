import numpy as np
import pandas as pd
from datetime import datetime as dt
import add.functions as fn
import webbrowser
import os

df = pd.read_csv("add/dataset.csv")
print("La base de datos ya tiene una primara depuración \nde datos erroneos, nulos o vacios. A continuación, se \norganizan los formatos de 'FECHA' y 'HORA' \npara poder realizar operaciones y análisis de series \nde tiempo con los datos.")

# Solo se deja información de utilidad debido a que la 
# información de la celda contiene ruido.
# Cada una de las entradas de FECHA viene 
# al final con la misma hora. ( 01/01/2020 12:00:00 AM )
df["FECHA"] = df["FECHA"].apply(lambda x: x[:10])
df["FECHA"] = pd.to_datetime(df["FECHA"],format = '%m/%d/%Y')

# Caso similar con HORA donde la información relevante 
# se encuentra en medio del String. ( 1899-12-31T19:10:00.000 )
df["HORA"] = df["HORA"].apply(lambda x: x[11:16])
df["HORA"] = pd.to_datetime(df["HORA"],format ='%H:%M')

print("*** "*10)
print("Se imprime toda los parametros y su tipo de dato:\n",df.dtypes)
print("\n\nLista de vehículos registrados en los accidentes:")
print("*** "*10)
# exite otra forma de obtener los datos únicos de un atributo:
# df.CLASE_DE_VEHICULOS.unique() pero el orden es por el mismo
# orden de aparicion en la columna CLASE_DE_VEHIVULO.
# El comando np.unique(df.CLASE_DE_VEHICULO) lo ordena de menor
# a mayor.
lista_vehiculos = np.unique(df.CLASE_DE_VEHICULO)
for item, vehiculos in enumerate(lista_vehiculos, start=1):
    print(item, vehiculos)

vehiculo_seleccionados = input("\nIngresar número a analizar o números separados por un espacio: ")
lista = fn.convert(lista_vehiculos,vehiculo_seleccionados)



# # Generar mapa con las opciones ingresadas
# fn.generarMapa(df,lista)

# # Abre el archivo map.html  
# filename = 'file:///'+os.getcwd()+'/' + 'map.html'
# webbrowser.open_new_tab(filename)