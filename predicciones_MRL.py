import pickle, os
from tkinter import *

#Creamos la clase predictions para almacenar las variables y su correlación
class Predictions:
    def __init__(self, x, y, x_title, y_title, punto_corte_x, m, b, correlation, bondad):
                                                    #La clase guarda la y, la y, el nombre de las respectivas columnas y su correlación
        self.x = x
        self.y = y
        self.x_title= x_title
        self.y_title = y_title
        self.correlation = correlation
        self.punto_corte_x = punto_corte_x
        self.m = m
        self.b = b
        self.bondad = bondad                          #La bondad de ajuste se calcula en el programa principal

    def load_file(window, file):
        with open(file, 'rb') as f:
            while True:                                 #mientras haya predicciones
                try:
                    prediccion = pickle.load(f)      #carga los datos 
                    new_window = Toplevel(window)
                    new_window.resizable(False, False)
                    new_window.title(str(file.split("/")[-1]))
                    Label(new_window, text=f"Variable X: {prediccion.x_title}: \n{prediccion.x}").pack(side=LEFT)
                    Label(new_window, text=f"Variable Y: {prediccion.y_title}: \n{prediccion.y}").pack(side=LEFT)
                    Label(new_window, text=f"Correlación: \n{prediccion.correlation:.4f}").pack(side=TOP)
                    Label(new_window, text=f"Bondad de ajuste: \n{prediccion.bondad:.4f}").pack(side=TOP)
                    break
                except EOFError:
                    break
