import pandas as pd
import add.functions as fn
import add.texto as tx
import webbrowser
import os

# cargando dataframe
df = pd.read_csv("add/dataset.csv")


if __name__=="__main__":
    # dando formato a los atributos de tiempo con "datetime"
    df = fn.darFormatoFecha(df)
    
    tx.intro()
    tx.info_dataframe(df)
    tx.separacion()
    tx.lista_vehiculos()
    # Prepara una lista de vehículos unica (sin repetir vehículo)
    # Imprime la lista en pantalla
    lista_vehiculos = fn.listaVehiculos(df)
    tx.separacion()
    # Espera el ingreso de los números de la lista asociados a los vehiculos
    seleccionando_vehiculos = input("\nIngresar número o números separados por un espacio: ")
    # Separa los nombres de los vehiculos de acuerdo a la lista de números seleccionados
    vehiculos_seleccionados = fn.convert(lista_vehiculos,seleccionando_vehiculos)
    # Crea gráfica general (todos los datos)
    # df_diario = fn.graficarHistorico(df)
    fn.creandoGraficas(fn.preparando_grafica(df,vehiculos_seleccionados))
    
    # seleccion_vehiculos_grafica = fn.preparando_grafica(df,lista)
    # print(seleccion_vehiculos_grafica)
    # # # Para generar el mapa solo descomenta las siguientes lineas de código
    # # # ------------------------------------------
    # # Generar mapa con las opciones ingresadas
    # fn.generarMapa(df,lista)

    # # Abre el archivo map.html  
    # filename = 'file:///'+os.getcwd()+'/'+'map.html'
    # webbrowser.open_new_tab(filename)