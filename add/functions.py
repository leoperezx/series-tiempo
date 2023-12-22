import folium
import numpy as np
import random
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statistics import multimode
from add.texto import prRed, prGreen, prYellow, prLightPurple, prPurple, prCyan, prLightGray, prBlack

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def listaVehiculos(df):
    # exite otra forma de obtener los datos únicos de un atributo:
    # df.CLASE_DE_VEHICULOS.unique() pero el orden es por el mismo
    # orden de aparicion en la columna CLASE_DE_VEHIVULO.
    # El comando np.unique(df.CLASE_DE_VEHICULO) lo ordena de menor
    # a mayor o alfabéticamente.
    lista_vehiculos = np.unique(df.CLASE_DE_VEHICULO)
    
    for item, vehiculos in enumerate(lista_vehiculos, start=1):
        print(item, vehiculos)

    return lista_vehiculos

def colores(vehiculos):
    # genera una lista de colores en formato hex [#xxyyzz]
    color_vehiculos = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(len(vehiculos))]
    return color_vehiculos

def convert(vehiculos,seleccion_de_vehiculos):
    '''
    Recibe los números ingresados por teclado, los asocia con la lista de 
    tipo de vehiculos y entrega la lista vinculando los vehículos. 
    '''
    # Divide con comas (,) los número ingresados por teclado
    li = list(seleccion_de_vehiculos.split(" ")) 
    # Cambia str a int elento por elemento
    res = [eval(i) for i in li] 
    # Resta uno a cada elemento de la lista
    lista = list(np.subtract(res, 1)) 
    # Asocia los numeros ingresados con la lista de vehículos
    seleccion = [ vehiculos[ lista[i] ] for i in range(len(lista))] 

    return seleccion
   
def darFormatoFecha(dataFrame):
    # Solo se deja información de utilidad debido a que la 
    # información de la celda contiene ruido.
    # Cada una de las entradas de FECHA viene 
    # al final con la misma hora. ( 01/01/2020 12:00:00 AM )
    dataFrame["FECHA"] = dataFrame["FECHA"].apply(lambda x: x[:10]) # se corta la información para toda la columna FECHA
    dataFrame["FECHA"] = pd.to_datetime(dataFrame["FECHA"],format = '%m/%d/%Y') # se le da formato datetime a lo que queda

    # Caso similar con HORA donde la información relevante 
    # se encuentra en medio del String. ( 1899-12-31T19:10:00.000 )
    dataFrame["HORA"] = dataFrame["HORA"].apply(lambda x: x[11:16])
    # print(dataFrame["HORA"])
    dataFrame["HORA"] = pd.to_datetime(dataFrame["HORA"])
    
    return dataFrame

def preparando_grafica(data,vehiculos_seleccionados):
    '''
    Función que entrega un diccionario donde las KEYs son los vehiculos seleccionados 
    y los valores son un conjunto Series de tiempo 
    {
        "seleccion1": "CLASE_DE_VEHICULO" : [Serie],
        "seleccion2": "CLASE_DE_VEHICULO" : [Serie], 
        .
        .
        
    }
    '''
    # Diccionario vacio
    datos_a_graficar = {}
    # iterando vehículos seleccionados
    for vehiculo in vehiculos_seleccionados:
        # se filtra la información por tipo de vehículo
        data_filter = data.loc[data['CLASE_DE_VEHICULO'].isin([vehiculo])]
        # se guarda, se agrupa y se cuenta las veces del accidente con la misma fecha (formto Series)
        datos_a_graficar[vehiculo] = pd.DataFrame(data_filter.groupby(["FECHA"])["CLASE_DE_VEHICULO"].agg('count'))
        
    return datos_a_graficar

def datosEstadisticos(data,vehiculos_seleccionados):
    
    cols = data.columns
    # print(data, vehiculos_seleccionados)
    data_filter = {}
    # iterando vehículos seleccionados
    for vehiculo in vehiculos_seleccionados:
        # se filtra la información por tipo de vehículo
        data_filter[vehiculo] = data.loc[data['CLASE_DE_VEHICULO'].isin([vehiculo])]
    
    
    print(cols)
    for item in data_filter:
        print("Vehículo: ",item)
        print("Lista de gravedad en accidentes: ",sorted(pd.unique(data_filter[item].GRAVEDAD)))
        print("La gravedad más frecuente: ")
        prRed(multimode(data_filter[item].GRAVEDAD))
        print("Lista de días de la semana en accidentes: ",sorted(pd.unique(data_filter[item].DIA_SEMANA)))
        print("El día de la semana más frecuente : ")
        prGreen(multimode(data_filter[item].DIA_SEMANA))
        print("Lista de la condición de la víctima: ",sorted(pd.unique(data_filter[item].CONDICION_DE_LA_VICTIMA)))
        print("La condición de la víctma más frecuente: ")
        prRed(multimode(data_filter[item].CONDICION_DE_LA_VICTIMA))
        print("Lista de la jornada del accidentes: ",sorted(pd.unique(data_filter[item].JORNADA)))
        print("La jornada más frecuente: ")
        prGreen(multimode(data_filter[item].JORNADA))
        print("Lista de las marcas del vehículo en accidentes: ",sorted(pd.unique(data_filter[item].MARCA)))
        print("La marca de vehículo más frecuente: ")
        prRed(multimode(data_filter[item].MARCA))
        print("cifras de lesionados en accidentes por día: ",sorted(pd.unique(data_filter[item].LESIONADO)))
        print("Cantidad de lesionados más frecuentes: ")
        prGreen(multimode(data_filter[item].LESIONADO))
        print("Cifras de homicidios en accidentes por día: ",sorted(pd.unique(data_filter[item].HOMICIDIOS)))
        print("Cantidad de homicidios más frecuentes: ")
        prRed(multimode(data_filter[item].HOMICIDIOS))
        print("* - "*10)
        print("\n")
        

def creandoSubGraficas(datos_vehiculos_seleccionados):
    num = len(datos_vehiculos_seleccionados)
    fig,ax=plt.subplots(num,1)
    
    print("width: {} | height: {} | dpi: {}".format(fig.get_figwidth(),fig.get_figheight(),fig.get_dpi())) 
    i = 0
    for vehiculos in datos_vehiculos_seleccionados:
        dt_grafica = datos_vehiculos_seleccionados[vehiculos]
        df_grafica = dt_grafica.CLASE_DE_VEHICULO.to_frame().reset_index()
        dfg = df_grafica.rename(columns = {"CLASE_DE_VEHICULO":"ACCIDENTES"})
                                                
        ax[i].plot(dfg["FECHA"], dfg["ACCIDENTES"],"-r",markersize=2)
        ax[i].set_xlabel("Tiempo - Año 2023", fontsize=10)
        ax[i].set_ylabel(vehiculos, fontsize=10)
        ax[i].xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
        ax[i].grid(True)
        i+=1
    
    fig.suptitle('Gráficas de accidentes de vehículos seleccionados', fontsize=16)
    fig.tight_layout(pad=1)
    plt.show()
    
def creandoGraficas(datos_vehiculos_seleccionados):
    # print(datos_vehiculos_seleccionados)    
    plt.style.use("tableau-colorblind10") #seaborn-whitegrid, Solarized_Light, ggplot
    plt.title("Gráfica de accidentes - Palmira 2020")
    plt.grid(True, which="minor", color="gray")
    
    for items in datos_vehiculos_seleccionados:
        # cada item es una serie de tiempo y se grafica directamente.
        dt_grafica = datos_vehiculos_seleccionados[items]
        # acumula las diferentes graficas
        plt.plot(dt_grafica.CLASE_DE_VEHICULO,marker="o")
        # imprime la etiquetas de los vehículos seleccionados.
        plt.ylabel(items)
    # imprime las gráficas
    plt.show()

def graficarHistorico(data):
    # preparando la información
    historico = data.groupby(["FECHA"]).size().reset_index(name="ACCIDENTES")
    # grafica
    plt.style.use("tableau-colorblind10") #seaborn-whitegrid, Solarized_Light, ggplot
    historico.plot.line(x="FECHA", y="ACCIDENTES")
    plt.ylabel("Número de accidentes.")
    plt.title("Gráfica de accidentes en 2020 en Palmira.")
    plt.show()   

# Pendiente de hacer un analisis de frecuencia.
# https://relopezbriega.github.io/blog/2016/09/26/series-de-tiempo-con-python/

# pendiente de partir esta funcion en dos funciones. Una que prepare y otra que grafique el mapa
def generarMapa(data,opciones):

    # Me recervo los colores: 'red' y'white'
    COLORS_BASE = ['darkgreen', 'darkred', 'darkblue', 'darkpurple', 'orange', 'purple', 'blue', 'lightgray', 'pink', 'lightblue', 'lightgreen', 'lightred', 'gray', 'beige', 'cadetblue', 'green'] 
    # Toma la cantidad de colores necesarios según la cantidad de opciones seleccionadas.
    COLORS_SELECTED=COLORS_BASE[:len(opciones)]

    for j in range(len(opciones)):
        # imprime una tabla de conversión.
        print("* - "*20 + "\n")
        print("Los vehículos {} son los puntos {}.\n".format(opciones[j], COLORS_SELECTED[j]))

    # Filtra de todo el dataframe solo los vehículos secionados.
    data_filter = data.loc[data['CLASE_DE_VEHICULO'].isin(opciones)] 

    data['COLOR'] = '' # crea una columna nueva llamada COLOR que sin datos.
    dataframe = pd.DataFrame() # crea un dataframe vacio sin datos.

    # Juntando información en el nuevo dataframe
    for index in range(len(opciones)):
        # Guarda la información por tipo de vehículo.
        data_filter = data.loc[data['CLASE_DE_VEHICULO'].isin( [opciones[index]] )]
        # Guarda un color por tipo de vehículo.
        data_filter['COLOR'] = COLORS_SELECTED[index]
        # prerando la data para graficar series de tiempo
        data_vehiculos = preparando_grafica(data,opciones)
        # Apila la información.
        dataframe = dataframe._append(data_filter)
    
    # print(data_vehiculos)
      
    some_map = folium.Map(location=(3.535513,-76.297656),tiles="cartodbpositron", zoom_start=10)

    tool_tip="Click me!"    


    for row in dataframe.itertuples():
        pop_up=("<p>Choque de vehículo tipo: " + row.CLASE_DE_VEHICULO +"</p>" +
                    "<p>Nivel de gravedad:" + row.GRAVEDAD + "</p>" + 
                    "<p>Hipótesis del accidente:" + row.HIPOTESIS + "</p>")
        
        folium.Marker([row.LAT,row.LONG], popup=pop_up, tooltip=tool_tip, icon=folium.Icon(color=row.COLOR,icon_color='black')).add_to(some_map) 
        # color='#F1F2F6',icon_color='#FFABAB'

    return some_map.save("map.html")
