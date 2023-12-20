import unittest, pandas, pickle, random
from tkinter import *
from tkinter.messagebox import showerror
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Predictions:
    '''
    Clase para guardar las predicciones de los modelos de regresión lineal.
    '''
    punto_corte_x: float
    x_title: str
    y_title: str
    m: float
    b: float
    error: float
    bondad: float
    description: str

class TestPredicciones(unittest.TestCase):
    def test_calculo_predicciones(self):
        counter = 0
        while counter < 100:
            try:
                x_value = random.randint(1,100)                                       # Cojemos el valor de x introducido por el usuario      
                y_title = "latitud"
                m = random.randint(1, 100)                         # Pendiente de la recta
                b = random.randint(1, 100)                         # Ordenada en el origen de la recta
                y_prediction = m * x_value + b                                              # Prediccion de y

                # Modificamos el label de la ecuacion de la recta para mostrar la prediccion de y
                ecuacion_label = Text()
                ecuacion_label.insert("1.0", f"{y_title} = {m:.4f}*({x_value}) + {b:.4f}")
                prediction_final = Text()
                prediction_final.insert("1.0", f"{y_prediction:.4f}")
                counter += 1
            except ValueError:
                showerror("Error", "El valor de x debe ser un número")
                
    def test_punto_corte(self):
        counter = 0
        while counter < 100:
            # m = 0 produce fallo con el assertNotEqual
            m = random.randint(1, 100)                         # Pendiente de la recta
            b = random.randint(1, 100)                         # Ordenada en el origen de la recta
            self.assertNotEqual(m, 0)
            if m != 0:
                punto_corte_x = -b / m                                                      # Punto de corte en el eje x
            else:
                raise ValueError("La pendiente de la recta no puede ser 0")
            counter += 1
    def test_get_description(self):
        description = Text()
        description.insert("1.0", "Esto es una descripcion")
        self.assertEqual(description.get("1.0", "end-1c"), "Esto es una descripcion")
        
    def test_graph(self):
        x = [1,2,3,4,5]
        y = [1,2,3,4,5]
        x_title = "latitud"
        y_title = "longitud"
        y_pred = [1,2,3,4,5]
        self.assertEqual(x, [1,2,3,4,5])
        self.assertEqual(y, [1,2,3,4,5])
        self.assertEqual(x_title, "latitud")
        self.assertEqual(y_title, "longitud")
        self.assertEqual(y_pred, [1,2,3,4,5])
        
        fig = plt.figure()                                                              # Creamos la figura
        ax = fig.gca()                                                                  # Cojemos los ejes
        ax.scatter(x, y)                                                                # Pintamos los puntos
        ax.plot(x, y_pred, color = 'red', linewidth = 2, label = 'Regresión lineal')    # Pintamos la recta de regresion lineal
        ax.legend()                                                                     # Mostramos la leyenda
        ax.set_xlabel(x_title)                                                          # Ponemos el titulo del eje x
        ax.set_ylabel(y_title)                                                          # Ponemos el titulo del eje y                         
        ax.set_title('Regresión Lineal y Correlación entre X e Y')                      # Ponemos el titulo del grafico
        self.assertRaises(TypeError, ax.scatter)

class TestGui(unittest.TestCase):
    def test_open_file(self):
        file_type = ["csv", "db", "xlsx"]
        self.assertRaises(FileNotFoundError, open, "doc_pruebas_unitarias\\test_file.csv")
        self.assertRaises(FileNotFoundError, open, "doc_pruebas_unitarias\\test_file.xlsx")
        self.assertRaises(FileNotFoundError, open, "doc_pruebas_unitarias\\test_file.db")
        
        self.assertIn("csv", file_type)
        self.assertIn("db", file_type)
        self.assertIn("xlsx", file_type)
        
    def test_save_file(self):
        # no deja con el path normal; hay que poner el path completo no se por que
        file = "C:\\Users\\Pablo\\Desktop\\practicaIS\\doc_pruebas_unitarias\\test_save.pkl"
        if file:                                                            # If the file already exists
            with open(file, 'wb') as f:                                     # Abriremos el archivo en modo escritura binaria
                pickle.dump(Predictions, f)                                  # Guardamos el objeto en el archivo
    def test_create(self):
        variable_x = "longitude"                                                # Variable para guardar la variable x
        variable_y = "latitude"                                                # Variable para guardar la variable y
        data = pandas.read_csv("C:\\Users\\Pablo\\Desktop\\practicaIS\\doc_pruebas_unitarias\\test_file.csv")                 # Leemos el archivo csv
        self.assertEqual(variable_x, "longitude")
        self.assertEqual(variable_y, "latitude")
        
        if variable_x  == 'Select' or variable_y  == 'Select':    # Comprobamos que no haya valores nulos
            showerror("Error", "No se pueden introducir valores nulos")
            
        else:
            x_col = data[variable_x]          # Cojemos la columna de la variable x
            y_col = data[variable_y]          # Cojemos la columna de la variable y
            if x_col.equals(y_col):                 # Comprobamos que las variables no sean iguales       
                showerror("Error", "Las variables no pueden ser iguales")

            else:
                x_col_reshaped = x_col.values.reshape(-1, 1)  # Redimensionamos los valores de x
                y_col_reshaped = y_col.values.reshape(-1, 1)  # Redimensionamos los valores de y
                self.assertIsNotNone(x_col_reshaped)
                self.assertIsNotNone(y_col_reshaped)

if __name__ == "__main__":
    unittest.main()