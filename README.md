# Accicentes Palmira 2020 - Series de tiempo

## Iniciando con Machine Learning - ML

El siguiente es un proyecto que se desprende del respositorio "accidentes" el cual es la base del funcionamiento de un framework [Streamlit](https://leoperezx-accidentes-streamlit-app-bfl2xc.streamlit.app/), que en este momento puede que este "dormido" y halla que despertarlo.

El motivo de este segundo repositorio es trabajar más en la parte de filtros, manipulación y la analítica de los datos, pero no tanto en la parte visual.

Se plantea de forma inicial solo usar _Python_ para este proyecto. En el directorio _add_ se encuentra un archivo con _funciones.py_ y la base de datos inicial. Además se encuetra un archivo _texto.py_ que modifica los textos de respuesta en la terminal para hacerlos resaltar.

## Información de la base de datos

Se realiza un trabajo previo para organizar la información de la base de datos. Inicialmente se _limpia_ la información contenida en **FECHA**, **AÑO**, **HORA** y **DIA_SEMANA** para mejorar, entender y manipular mejor la información y las respuestas. Se desarrollan algunas funciones para dibujar en un mapa cada uno de los puntos georeferenciados realizando algunos filtros. Se recuerda que la información aquí consignada es información de _datos abiertos_ de la _Alcaldía de Palmira_ de los accidentes registrados en el año 2020.

A continuación, se muestra la lista disponible de atributos de la base de datos:
    - GRAVEDAD
    - FECHA
    - AÑO
    - HORA
    - JORNADA
    - DIA_SEMANA
    - BARRIOS_CORREGIMIENTO_VIA
    - DIRECCION
    - ZONA
    - AUTORIDAD
    - LAT
    - LONG
    - HIPOTESIS
    - CONDICION_DE_LA_VICTIMA
    - CLASE_DE_SINIESTRO
    - LESIONADO
    - HOMICIDIOS
    - CLINICA
    - SITIO
    - CLASE_DE_VEHICULO
    - MARCA
    - MATRICULA
    - TIPO_DE_SERVICIO
    - EMPRESA

La información contenida en _dataset.csv_ ya fue inicialmente limpidada. Sin embargo exiten alugunas impuresas que se corregirán a medida que se requiera pulir la información.

## Requirements

En el archivo _requirements.txt_ se encuentran los paquetes de Python que he utilizado para este pequeño Script.

## Patallazos

El dataframe aloja información de los accidentes en Palmira ocurridos en el año 2020. Por ahora he filtrado la información por tipo de vehículo logrando que el usuario del algoritmo pueda seleccionar que tipo de vehículo quiere ver en un mapa. Cuando se ejecuta el script este solo pregunta por el número asociado a los vehículos de interes.

![lista de vehículos](/add/presentacion.PNG)

Puedes escribir más de un número de interes separado los números con un espacio (Ej. 2 3 10 13). El algoritmo espera números del 1 al 16. Cada número se asocia a una solicitid de información. Se extrae toda la información y se junta toda en un dataframe mas pequeño. Además se le asocia un color diferente a cada vihículo dentro del dataframe.

![lista de vehículos](/add/presentacion1.PNG)

El algoritmo realiza una pequeña tabla de conveción presentada en la terminal.

![lista de vehículos](/add/presentacion2.PNG)

Al final, el agoritmo abre un navegador y debe mostrar en un mapa una serie de puntos los accidentes asociados diferenciado por color. Cada punto muestra una pequeña información adicional y particular dando "click" sobre. la velocidad con la que se genera el mapa y la interacción depende de muchas cosas, entre ellas de la velocidad de tu computadora.

![lista de vehículos](/add/presentacion3.PNG)

La anterior imágen es un ejemplo de como debe ser el resultado final.

## Gráficas

Al realizar la selección de vehículos se realiza la programación de un función para realizar una gráfica. Esta solo grafica los vehículos seleccionados. en adelante se busca realizar muchos tipos de gráficas relacionadas con estadística.

> &copy; 2023 | [leoperezx](https://linkr.bio/2op3pq)
