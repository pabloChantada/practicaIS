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

    # Creamos el modelo de regresion lineal
    model = LinearRegression().fit(x, y)
    # Predecimos los valores de y
    y_pred = model.predict(x)

    # Coeficiente de la recta
    m = model.coef_[0][0]
    # Termino independiente de la recta
    b = model.intercept_[0]

    if m != 0:
        # Punto de corte en el eje x
        punto_corte_x = -b / m
    else:
        punto_corte_x = None

    # Error cometido
    error = mean_squared_error(y, y_pred)
    # Bondad de ajuste (R^2)
    bondad = model.score(x, y)

    # Graficamos y generamos los labels
    description_var = graph(window, x, y, x_title, y_title, y_pred)

    # Guardamos los resultados de la regresion lineal en una clase

    prediction = Predictions(punto_corte_x, x_title,
                             y_title, m, b, error, bondad, description_var)

    return prediction


def generate_labels(window, x_title: str, y_title: str):
    '''
    Elimina los elementos de la ventana y crea los nuevos labels.

    Parametros:
    --------------

    window: Ventana master
    x_title: Nombre de la columna x del dataframe
    x: Columna x seleccionada del dataframe
    '''
    global graph_labels, bondad_label, ecuacion_label, error_label, \
        select_x_entry, prediction_button, select_x_label, description, predicition_var, prediction_title, prediction_final, x_var_tiltle

    # Eliminamos los labels anteriores
    if 'graph_labels' in globals() and graph_labels is not None:
        graph_labels.destroy()

    # Creamos el frame para los labels
    graph_labels = Frame(window)
    # Posicion del frame
    graph_labels.pack(side=BOTTOM)

    description_label = Label(graph_labels, text=f"Descripción:")
    description_label.grid(row=0, column=0, pady=1, sticky="w")
    scrollbar = Scrollbar(graph_labels)
    scrollbar.grid(row=1, column=1, sticky='ns')
    # Creamos el label de la descripcion
    description = Text(graph_labels, height=3, width=30,
                       yscrollcommand=scrollbar.set)
    # Posicion de la descripcion
    description.grid(row=1, column=0, sticky="w")
    scrollbar.config(command=description.yview)

    # -------------------ECUACION DE LA RECTA Y BOTON DE PREDICCION-------------------
    ecuacion_label = Label(
        graph_labels, text=f"{y_title} = {m:.4f}*({x_title}) + {b:.4f}")
    ecuacion_label.grid(row=2, column=0, pady=1, sticky="w")

    x_var_tiltle = Label(
        graph_labels, text=f"Variable de x para la predicción: {x_title} = ")
    x_var_tiltle.grid(row=3, column=0, pady=1, sticky="w")

    predicition_var = Entry(graph_labels, width=10)
    predicition_var.grid(row=3, column=1, pady=1, sticky="w")
    prediction_button = Button(graph_labels, text="Predecir", width=10,
                               command=lambda: generate_prediction(y_title))
    prediction_button.grid(row=3, column=2, pady=1, sticky="w")
    prediction_title = Label(graph_labels, text=f"{y_title} = ")
    prediction_title.grid(row=3, column=3, pady=1, sticky="w")
    prediction_final = Label(graph_labels, text=f"")
    prediction_final.grid(row=3, column=4, pady=1, sticky="w")

    # -------------------BONDAD DE AJUSTE Y ERROR COMETIDO-------------------
    bondad_label = Label(
        graph_labels, text=f"Bondad de ajuste (R^2): {bondad:.4f}")
    bondad_label.grid(row=4, column=0, pady=1, sticky="w")

    error_label = Label(graph_labels, text=f"Error cometido: {error}")
    error_label.grid(row=5, column=0, pady=2, sticky="w")


def generate_prediction(y_title: str):
    '''
    Genera una prediccion de y para un valor de x.

    Parametros:
    --------------

    x: Columna x seleccionada del dataframe
    '''
    global PREDICTION_COUNTER
    try:

        # Cojemos el valor de x introducido por el usuario
        x_value = float(predicition_var.get())

        # Prediccion de y
        y_prediction = m * x_value + b

        # Modificamos el label de la ecuacion de la recta para mostrar la prediccion de y

        ecuacion_label.config(
            text=f"{y_title} = {m:.4f}*({x_value}) + {b:.4f}")
        prediction_final.config(text=f"{y_prediction:.4f}")

        # Incrementamos el contador de predicciones
        PREDICTION_COUNTER += 1

        # Mostramos la prediccion en el grafico
        ax.scatter(x_value, y_prediction, color='black', marker='o',
                   label=f'Predicción {PREDICTION_COUNTER}')
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

    # Creamos la figura
    fig = plt.figure()
    # Cojemos los ejes
    ax = fig.gca()
    # Pintamos los puntos
    ax.scatter(x, y)
    # Pintamos la recta de regresion lineal
    ax.plot(x, y_pred, color='red', linewidth=2, label='Regresión lineal')
    # Mostramos la leyenda
    ax.legend()
    # Ponemos el titulo del eje x
    ax.set_xlabel(x_title)
    # Ponemos el titulo del eje y
    ax.set_ylabel(y_title)
    # Ponemos el titulo del grafico
    ax.set_title('Regresión Lineal y Correlación entre X e Y')

    # ====================GENERACION DE LABELS====================

    # Generamos los labels
    generate_labels(window, x_title, y_title)

    # ====================GRAFICO====================
    # Creamos el canvas
    canvas = FigureCanvasTkAgg(fig, master=window)
    # Posicion del canvas
    canvas.get_tk_widget().pack(side=LEFT)
