from tkinter import *
from dataclasses import dataclass
from tkinter.messagebox import showerror

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
           
def generate_labels_prediction(window, prediction: object):
    '''
    Genera los labels para mostrar la ecuacion de la recta, la bondad de ajuste y el error cometido del archivo pkl.

    Parametros:
    --------------

    window: Ventana master
    prediction: Objeto que guarda la predicción
    '''

    global graph_labels, bondad_label, ecuacion_label, error_label, \
        select_x_entry, prediction_button, select_x_label, description,\
        prediction_title, prediction_final, predicition_var
    
    # Eliminamos los labels anteriores
    if 'graph_labels' in globals() and graph_labels is not None:
        graph_labels.destroy()

    graph_labels = Frame(window)                                            # Creamos el frame para los labels
    graph_labels.pack(side=BOTTOM)                                          # Posicion del frame

    description = Text(graph_labels, height = 3, width = 30)                # Create the label for the description
    description.grid(row = 0, column = 0)                                   # Position the label
    description.insert(END, prediction.description)                         # Insertamos una descripcion
    
    # -------------------ECUACION DE LA RECTA Y BOTON DE PREDICCION-------------------
    ecuacion_label = Label(graph_labels, text = f"Ecuación de la recta: {prediction.m:.4f}x + {prediction.b:.4f} = y")
    ecuacion_label.grid(row = 1, column = 0, pady = 1, sticky = "w")

    # Usamos lambda para generar una funcion anonima que nos permita pasarle argumentos a la funcion generate_prediction2
    # sin que se ejecute automaticamente al crear el boton

    x_var_tiltle = Label(graph_labels, text = f"Variable de x para la predicción: {prediction.x_title} = ")
    x_var_tiltle.grid(row = 2, column = 0, pady = 1, sticky = "w")
    predicition_var = Entry(graph_labels, width = 10)
    predicition_var.grid(row = 2, column = 1, pady = 1, sticky = "w")
    prediction_button = Button(graph_labels, text = "Predecir", width = 10, \
                        command = lambda: generate_prediction2(prediction))
    prediction_button.grid(row = 2, column = 2, pady = 1, sticky = "w")

    prediction_title = Label(graph_labels, text = f"{prediction.y_title} = ")
    prediction_title.grid(row = 2, column = 3, pady = 1, sticky = "w")
    prediction_final = Label(graph_labels, text = f"")
    prediction_final.grid(row = 2, column = 4, pady = 1, sticky = "w")

    # -------------------BONDAD DE AJUSTE Y ERROR COMETIDO-------------------
    bondad_label = Label(graph_labels, text = f"Bondad de ajuste (R^2): {prediction.bondad:.4f}")
    bondad_label.grid(row = 3, column = 0, pady = 1, sticky = "w")
    
    error_label = Label(graph_labels, text=f"Error cometido: {prediction.error}")
    error_label.grid(row = 4, column = 0, pady = 2, sticky="w")
    
def generate_prediction2(prediction: object):
    '''
    Genera una prediccion de y para un valor de x del archivo pkl.

    Parámetros:
    --------------
    prediction: Objeto que guarda la predicción
    '''
    try:
        x_value = float(predicition_var.get())                             # Valor de x para generar la prediccion de y

        y_prediction = prediction.m * x_value + prediction.b              # Prediccion de y
        
        # Modificamos el label de la ecuacion de la recta para mostrar la prediccion de y
        ecuacion_label.config(text = f"{prediction.y_title} = {prediction.m:.4f}*({x_value}) + {prediction.b:.4f}")
        prediction_final.config(text = f"{y_prediction:.4f}")

    except ValueError:
        showerror("Error", "El valor de x debe ser un número")