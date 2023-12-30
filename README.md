# DEPENDENCIAS

Para modificar el codigo fuente es necesario instalar las siguientes librerias:
- pandas
- sqlite3
- pickle
- tkinter
- pandastable
- matplotlib
- sklearn
O usando una de estas intalaciones:
```pip install pandas sqlite3 pickle tkinter pandastable matplotlib sklearn```
```python -m pip install pandas sqlite3 pickle tkinter pandastable matplotlib sklearn```

Además, de tener Python 3.10 o superior.

# MANUAL DE USUARIO

## DESCARGA

Para la descarga del progama selecionar la pestaña de __Releases__en la parte 
derecha de la página y seleccionar la versión deseada. 

## EJECUCIÓN

Para iniciar el progama abrimos el archivo gui.exe y se ejecutara autmaticamente
el progama. Una vez iniciado el progama tenemos dos opciones: _Crear un modelo_ o
_Cargar un modelo_

### Crear modelo

Para crear un nuevo modelo debemos seleccionar en la pestaña __File__
y a continuación pulsar __Open File__. Seleccionamos un archivo para abrir los
datos con una de las siguientes extensiones aceptadas:

- *.csv
- *.xlsx
- *.db

A continuación se muestra un datagrama con los datos seleccionados y un menú
desplegable en el que seleccionar las variables del modelo. Tras seleccionar las
variables pulsamos __Crear Modelo__ para generar el modelo.

Dentro del modelo tenemos la opción de __Predecir__; con ella podemos modificar la 
recta de regresión lineal para obtener el valor de __y__ para un valor de __x__ 
seleccionado.

### Cargar modelo

Para cargar un modelo debemos seleccionar un archivo en la pestaña __File__ , a 
continuación pulsar __Load Model__ y seleccionar un archivo __*.pkl__. Dentro de 
este modelo se pueden hacer predicciones de la variable __y__ de la recta de 
regresión lineal para un valor de __x__, sin embargo _no se pueden seleccionar nuevas
columnas_

### Guardar modelo

Para guardar el modelo actual, debemos seleccionar la pestaña __File__
y a continuación pulsar __Save File__
