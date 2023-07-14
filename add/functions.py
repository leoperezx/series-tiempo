import folium
import numpy as np
import random

def colores(vehiculos):
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
    # Resta uno a cada elemeto de la lista
    lista = list(np.subtract(res, 1)) 
    # Asocia los numeros ingresados con la lista de vehículos
    seleccion = [ vehiculos[ lista[i] ] for i in range(len(lista))] 

    return seleccion
    

def generarMapa(data,opciones):
    '''
    Organiza la información de la base de datos para dibujar en un mapa 
    cada uno de los puntos georeferenciados para ubicar cada uno de los 
    accidentes registrados en el año 2020 en Palmira. 

    lista disponible de atributos de la base de datos son:
    GRAVEDAD,
    FECHA,
    AÑO,
    HORA,
    JORNADA,
    DIA_SEMANA,
    BARRIOS_CORREGIMIENTO_VIA,
    DIRECCION,
    ZONA,
    AUTORIDAD,
    LAT,
    LONG,
    HIPOTESIS,
    CONDICION_DE_LA_VICTIMA,
    CLASE_DE_SINIESTRO,
    LESIONADO,
    HOMICIDIOS,
    CLINICA,
    SITIO,
    CLASE_DE_VEHICULO,
    MARCA,
    MATRICULA,
    TIPO_DE_SERVICIO,
    EMPRESA,,

    '''
    
    print( colores(opciones) ) # crea tantos colores aleatorios como vehiculos selecionados 

    data_filter = data.loc[data['CLASE_DE_VEHICULO'].isin(opciones)] 

    # for index in opciones:
    #     print(opciones[index])

    # for index in opciones:
    #     data_filter["color"] = data.loc[data['CLASE_DE_VEHICULO'].isin(opciones[index])] 
    
    # print(data_filter.head())
    
    some_map = folium.Map(location=(3.535513,-76.297656),tiles="cartodbpositron", zoom_start=10)

    tool_tip="Click me!"    


    for row in data_filter.itertuples():
        pop_up=("<p>Choque de vehículo tipo: " + row.CLASE_DE_VEHICULO +"</p>" +
                    "<p>Nivel de gravedad:" + row.GRAVEDAD + "</p>" + 
                    "<p>Hipótesis del accidente:" + row.HIPOTESIS + "</p>")
        
        folium.Marker([row.LAT,row.LONG], popup=pop_up, tooltip=tool_tip, icon=folium.Icon(color='#F1F2F6',icon_color='#FFABAB')).add_to(some_map)

    return some_map.save("map.html")
