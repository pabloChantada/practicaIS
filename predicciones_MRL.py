import pickle
import os

#Creamos la clase predictions para almacenar las variables y su correlación
class Predictions:
    def __init__(self, x, y, x_title, y_title, punto_corte_x, m, b, correlation):
                                                    #La clase guarda la y, la y, el nombre de las respectivas columnas y su correlación
        self.x = x
        self.y = y
        self.x_title= x_title
        self.y_title = y_title
        self.punto_corte_x = punto_corte_x
        self.m = m
        self.b = b
        self.correlation = correlation

    def __str__(self):                              #la cadena que devuelve representa una instancia de esa clase       
        return f"Predicción para {self.x_title}: {self.x}, {self.y_title}: {self.y} -> Correlación: {self.correlation}"


# Función para guardar una predicción en memoria usando pickle
def guardar_prediccion(prediction, archivo):
    if os.path.exists(archivo):                     #si ya existe el archivo predicciones.plk
        with open(archivo, 'ab') as file:           #abrimos el archivo en modo binario para añadir 
            pickle.dump(prediction, file)           #las predicciones al final del archivo

    else:                                           #si no existe el archivo predicciones.plk         
        with open(archivo, 'wb') as file:           #creamos un archivo en modo binario
            pickle.dump(prediction, file)           #para escribir la primera prediccion


# Función para cargar las predicciones desde el archivo usando pickle
def cargar_predicciones(archivo):
    with open(archivo, 'rb') as file:               #lee el archivo 
        while True:                                 #mientras haya predicciones
            try:
                prediccion = pickle.load(file)      #carga los datos 
                yield prediccion                    #en cada iteración devuelve una predicción
            except EOFError:
                break                        
    

