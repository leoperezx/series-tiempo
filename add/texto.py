
def intro():
    print("La base de datos ya tiene una primara depuración \nde datos erroneos, nulos o vacios. A continuación, se \norganizan los formatos de 'FECHA' y 'HORA' \npara poder realizar operaciones y análisis de series \nde tiempo con los datos.")

def info_dataframe(dataframe):
    print("*** "*10)
    print("Se imprime toda los parametros y su tipo de dato:\n",dataframe.dtypes)
    
def lista_vehiculos():
    print("\n\nLista de vehículos registrados en los accidentes:")
    print("*** "*10)
    
def separacion():
    print("* - "*20)