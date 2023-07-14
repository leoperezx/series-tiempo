# Series de tiempo

## Iniciando con Machine Learning - ML

El siguiente es un proyecto que se desprende del respositorio "acciedentes" el cual es la base del funcionamiento de un framework [Streamlit](https://leoperezx-accidentes-streamlit-app-bfl2xc.streamlit.app/), que en este momento puede que este "dormido" y tengas que despertarlo.

El motivo de este segundo repositorio es trabajar mas en la parte de filtros, manipulación y la analítica de los datos, pero no tanto en la parte visual.

Se plantea de forma inicial solo usar _Python_ para este proyecto. En el directorio _add_ se encuentra un archivo con funciones y la base de datos inicial.

## Requirements

En el archivo _requirements.txt_ se encuentran los paquetes de Python que he utilizado para este pequeño Script. 

## Patallazos

El dataframe aloja información de los accidentes en Palmira ocurridos en el año 2020. Por ahora he filtrado la información por tipo de vehículo logrando que el usuario del algoritmo pueda seleccionar que tipo de vehículo quiere ver en un mapa. Cuando se ejecuta el script este solo pregunta por el número asociado a los vehículos de interes.

![lista de vehículos](/add/presentacion.PNG)

Puedes escribir más de uno separados por un espacio. El algoritmo espera números del 1 al 16. Cada número se asocia a una solicitid de información. Se extrae toda la información y se junta toda en un dataframe mas pequeño. Además se le asocia un color diferente a cada vihículo dentro del dataframe.

![lista de vehículos](/add/presentacion1.PNG)

El algoritmo realiza una pequeña tabla de conveción.

![lista de vehículos](/add/presentacion2.PNG)

Al final, presenta una serie de puntos en un mapa. Cada punto muestra una pequeña información adicional y particular de cada accidente. la velocidad con la que se genera el mapa depende de muchas cosas, entre ellas de la velocidad de tu computadora.

![lista de vehículos](/add/presentacion3.PNG)

La anterior imgen es un ejemplo de como debe ser el resultado final.

> &copy; 2023 LeoPerez: [@leoperezx](https://linkr.bio/2op3pq)