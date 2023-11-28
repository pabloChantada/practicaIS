import pickle
from tkinter import *
from dataclasses import dataclass

#Creamos la clase predictions para almacenar los datos de los MRL.
@dataclass
class Predictions:
    punto_corte_x: float
    m: float
    b: float
    error: float
    bondad: float
    description: str
        
    @classmethod
    def load_file(window, file):
        with open(file, 'rb') as f:
            while True:                                 #mientras haya predicciones
                try:
                    prediccion = pickle.load(f)         #carga los datos 
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