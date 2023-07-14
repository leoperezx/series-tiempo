# Series de tiempo

## Iniciando con Machine Learning - ML

El siguiente es un proyecto que se desprende del respositorio "acciedentes" el cual es la base del funcionamiento de un framework [Streamlit](https://leoperezx-accidentes-streamlit-app-bfl2xc.streamlit.app/), que en este momento puede que este "dormido" y tengas que despertarlo.

El motivo de este segundo repositorio es trabajar mas en la parte de filtros, manipulación y la analítica de los datos, pero no tanto en la parte visual.

Se plantea de forma inicial solo usar _Python_ para este proyecto. En el directorio _add_ se encuentra un archivo con funciones y la base de datos inicial.

## Requirements

En el archivo _requirements.txt_ se encuentran los paquetes de Python que he utilizado para este pequeño Script. 

## Patallazos

El dataframe aloja información de los accidentes en Palmira ocurridos en el año 2020. Por ahora he filtrado la información por tipo de vehículo logrando que el usuario del algoritmo pueda seleccionar que tipo de vehículo quiere ver en un mapa. Cuando se ejecuta el script este solo pregunta por el número asociado a los vehículos de interes. Puedes escribir más de uno separados por un espacio. El algoritmo espera números del 1 al 16.

![lista de vehículos](/add/presentacion.PNG)

