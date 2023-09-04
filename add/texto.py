
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
 
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