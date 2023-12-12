import matplotlib.pyplot as plt
from tkinter import *
from tkinter.messagebox import showerror
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from predicciones_MRL import Predictions

# ====================CONSTANTES====================

PREDICTION_COUNTER = 0
ecuacion_label = None
bondad_label = None
error_label = None
select_x_entry = None
prediction_button = None
select_x_label = None
description = None

def modelo_regresion_lineal(window, x: list, y: list, x_title: str, y_title: str):
    '''
    Muestra el grafico de regresion lineal, la ecuacion de la recta, la bondad de ajuste, el error cometido
    y devuelve la prediccion.

    Parámetros:
    --------------

    window: Ventana master
    x: Columna x seleccionada del dataframe
    y: Columna y seleccionada del dataframe
    x_title: Nombre de la columna x del dataframe
    y_title: Nombre de la columna y del dataframe
    '''               
    global bondad, m, b, error

    model = LinearRegression().fit(x, y)                       # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                  # Predecimos los valores de y

    m = model.coef_[0][0]                                      # Coeficiente de la recta
    b = model.intercept_[0]                                    # Termino independiente de la recta

    punto_corte_x = -b/m                                       # Punto de corte en el eje x

    error = mean_squared_error(y, y_pred)                      # Error cometido
    bondad = model.score(x, y)                                 # Bondad de ajuste (R^2)

    description_var = graph(window, x, y, x_title, y_title, y_pred)  # Graficamos y generamos los labels
    # Guardamos los resultados de la regresion lineal en una clase
    prediction = Predictions(punto_corte_x, x_title, m,b, error,bondad, description_var)
    return prediction

def generate_labels(window, x_title: str, x: list): 
    '''
    Elimina los elementos de la ventana y crea los nuevos labels.

    Parametros:
    --------------

    window: Ventana master
    x_title: Nombre de la columna x del dataframe
    x: Columna x seleccionada del dataframe
    '''
    global graph_labels, bondad_label, ecuacion_label, error_label, \
        select_x_entry, prediction_button, select_x_label, description, prediction_label
        
    # Eliminamos los labels anteriores
    if 'graph_labels' in globals() and graph_labels is not None:
        graph_labels.destroy()

    graph_labels = Frame(window)                            # Creamos el frame para los labels
    graph_labels.pack(side=BOTTOM)                          # Posicion del frame

    description = Text(graph_labels, height=3, width=30)    # Creamos el label de la descripcion
    description.grid(row=0, column=0)                       # Posicion de la descripcion
    description.insert(END, "Descripción: ")                # Insertamos una descripcion
    
    # -------------------ECUACION DE LA RECTA Y BOTON DE PREDICCION-------------------
    ecuacion_label = Label(graph_labels, text=f"Ecuación de la recta: {m:.4f}x + {b:.4f} = y")
    ecuacion_label.grid(row=1, column=0, pady=1, sticky="w")

    prediction_button = Button(graph_labels, text="Predecir", width=15, command=lambda: generate_prediction(x))
    prediction_button.grid(row=1, column=1, pady=1, sticky="w")

    prediction_label = Label(graph_labels, text=f"")
    prediction_label.grid(row=2, column=0, pady=1, sticky="w")

    # -------------------VALOR DE X PARA GENERAR LA PREDICCION DE Y-------------------
    select_x_label = Label(graph_labels, text="Valor de x para generar la prediccion de y: ")
    select_x_label.grid(row=3, column=0, pady=1, sticky="w")

    select_x_entry = Entry(graph_labels, width=20)
    select_x_entry.insert(0, x_title)
    select_x_entry.grid(row=3, column=1, pady=1, sticky="w")
    
    # -------------------BONDAD DE AJUSTE Y ERROR COMETIDO-------------------
    bondad_label = Label(graph_labels, text=f"Bondad de ajuste (R^2): {bondad:.4f}")
    bondad_label.grid(row=4, column=0, pady=1, sticky="w")
    
    error_label = Label(graph_labels, text=f"Error cometido: {error}")
    error_label.grid(row=5, column=0, pady=2, sticky="w")

def generate_prediction(x:  list):
    '''
    Genera una prediccion de y para un valor de x.

    Parametros:
    --------------

    x: Columna x seleccionada del dataframe
    '''
    global PREDICTION_COUNTER
    try:
        x_value = float(select_x_entry.get())      # Cojemos el valor de x introducido por el usuario      
        if x_value < min(x) or x_value > max(x):
            showerror("Error", "El valor de x debe estar entre los valores de x de la muestra")
            return
        
        y_prediction = m * x_value + b              # Prediccion de y

        # Modificamos el label de la ecuacion de la recta para mostrar la prediccion de y
        ecuacion_label.config(text=f"Ecuación de la recta: {m:.4f}*({x_value}) + {b:.4f} = {y_prediction:.4f}")
        prediction_label.config(text=f"Para x = {x_value:.2f}, la prediccion de y es {y_prediction:.2f}.")
        #ecuacion_label.config(text=f"Para x = {x_value:.2f}, la prediccion de y es {y_prediction:.2f}.")

        PREDICTION_COUNTER += 1                     # Incrementamos el contador de predicciones
        
        # Mostramos la prediccion en el grafico
        ax.scatter(x_value, y_prediction, color='black', marker='o', label=f'Predicción {PREDICTION_COUNTER}')
        ax.legend()  
        canvas.draw()

    except ValueError:
        showerror("Error", "El valor de x debe ser un número")
        
def get_description():
    '''
    Devuelve la descripcion actual del modelo.
    '''
    return description.get("1.0", "end-1c") 

def graph(window, x: list, y: list, x_title: str, y_title: str, y_pred: list):
    '''
    Genera el grafico de regresion lineal y los labels necesarios.

    Parametros:
    --------------
    
    window: Ventana master
    x: Columna x seleccionada del dataframe
    y: Columna y seleccionada del dataframe
    x_title: Nombre de la columna x del dataframe
    y_title: Nombre de la columna y del dataframe
    y_pred: Predicción del valor y a partir de un valor x    
    '''
    global fig, ax, canvas
    
    # Eliminamos los elementos de la ventana que no podemos con clear_labels()
    if 'fig' in globals():
        plt.close(fig)                
    if 'description' in globals() and description is not None:
        description.destroy()
    if 'canvas' in globals() and canvas is not None:
        canvas.get_tk_widget().destroy()
    
    fig = plt.figure()                                                      # Creamos la figura
    ax = fig.gca()                                                          # Cojemos los ejes
    ax.scatter(x, y)                                                        # Pintamos los puntos
    ax.plot(x, y_pred, color='red', linewidth=2, label='Regresión lineal')  # Pintamos la recta de regresion lineal
    ax.legend()                                                             # Mostramos la leyenda
    ax.set_xlabel(x_title)                                                  # Ponemos el titulo del eje x
    ax.set_ylabel(y_title)                                                  # Ponemos el titulo del eje y                         
    ax.set_title('Regresión Lineal y Correlación entre X e Y')              # Ponemos el titulo del grafico

    # ====================GENERACION DE LABELS====================
    
    generate_labels(window, x_title: str, x: list)                                        # Generamos los labels   
    
    # ====================GRAFICO====================

    canvas = FigureCanvasTkAgg(fig, master=window)                          # Creamos el canvas
    canvas.get_tk_widget().pack(side=LEFT)                                  # Posicion del canvas                 