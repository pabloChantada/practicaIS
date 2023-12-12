# MANUAL DE USUARIO

## DESCARGA

Para la descarga del progama selecionar la pestaña __CODE__ en el repositorio y
seleccionar la opción de __Descargar ZIP__.

## EJECUCIÓN

Para iniciar el progama tenemos tres opciones:

1. Linea de comandos con (estando en la carpeta inicial):
```python .\gui.py```
2. Ejecutando el codigo __gui.py__ en un IDE
3. _Ejecutando mrl.exe (aun no implementado)_

## Crear modelo

Para crear un nuevo modelo debemos seleccionar un archivo en la pestaña __File__
y a continuación pulsar __Open File__. Seleccionamos un archivo para insertar los
datos con una de las siguientes extensiones aceptadas:

- *.csv
- *.xlsx
- *.db

A continuación se muestra un datagrama con los datos seleccionados y un menú
desplegable en el que seleccionar las variables del modelo. Tras seleccionar las
variables pulsamos __Crear__ para generar el modelo.

Dentro del modelo tenemos la opción de __Predecir__; con ella podemos modificar la 
recta de regresión lineal para obtener el valor de __y__ para un valor de __x__ 
seleccionado.

## Cargar modelo

Para cargar un modelo debemos seleccionar un archivo en la pestaña __File__ , a 
continuación pulsar __Load Model__ y seleccionar un archivo __*.pkl__. Dentro de 
este modelo se pueden hacer predicciones de la variable __y__ de la recta de 
regresión lineal para un valor de __x__, sin embargo _no se pueden seleccionar nuevas
columnas_
