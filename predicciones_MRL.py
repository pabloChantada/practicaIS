import pickle, os
from tkinter import *
from tkinter.messagebox import showerror

#Creamos la clase predictions para almacenar las variables y su correlación
class Predictions:
    def __init__(self, x, y, x_title, y_title, punto_corte_x, m, b, correlation, bondad, description):
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
        self.description = description
        
    def save_to_file(self, file):
            data_to_save = {
                "x": self.x,
                "y": self.y,
                "x_title": self.x_title,
                "y_title": self.y_title,
                "correlation": self.correlation,
                "punto_corte_x": self.punto_corte_x,
                "m": self.m,
                "b": self.b,
                "bondad": self.bondad,
                "description": self.description
            }

            with open(file, 'wb') as file_stream:
                pickle.dump(data_to_save, file_stream)

    def load_file(window, file):
        try:
            with open(file, 'rb') as f:
                prediction = pickle.load(f)
                pickle.dump(prediction, file)

            new_window = Toplevel(window)
            new_window.resizable(False, False)
            new_window.title(os.path.basename(file))

            Label(new_window, text=f"Variable X ({prediction.x_title}):").grid(row=0, column=0, sticky="w")
            Label(new_window, text=str(prediction.x)).grid(row=0, column=1, sticky="w")

            Label(new_window, text=f"Variable Y ({prediction.y_title}):").grid(row=1, column=0, sticky="w")
            Label(new_window, text=str(prediction.y)).grid(row=1, column=1, sticky="w")

            Label(new_window, text=f"Correlación: {prediction.correlation:.4f}").grid(row=2, column=0, sticky="w")
            Label(new_window, text=f"Bondad de ajuste: {prediction.bondad:.4f}").grid(row=3, column=0, sticky="w")

        except (EOFError, pickle.UnpicklingError):
            showerror("Error", "Formato de archivo no válido o corrupto.")
