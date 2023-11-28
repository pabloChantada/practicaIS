import matplotlib.pyplot as plt
from tkinter import Label
from tkinter.messagebox import showerror
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from predicciones_MRL import *
import os

bondad_label = None
ecuacion_label = None
error_label = None
prediction_button = None
select_x_entry = None
select_x_label = None

def modelo_regresion_lineal(window, x, y, x_title, y_title):
    '''
    Muestra el grafico de regresion lineal, la ecuacion de la recta, la bondad de ajuste y el error cometido.
    '''               
    global bondad, m, b, bondad_label, ecuacion_label, description_var

    model = LinearRegression().fit(x, y)                       # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                  # Predecimos los valores de y
    m = model.coef_[0][0]                                      # Coeficiente de la recta
    b = model.intercept_[0]                                    # Termino independiente de la recta
    punto_corte_x = -b/m                                       # Punto de corte en el eje x
    error = mean_squared_error(y, y_pred)                      # Error cometido
    bondad = model.score(x, y)                                 # Bondad de ajuste (R^2)
    graph(window, x, y, x_title, y_title, y_pred, error)       # Graficamos y generamos los labels
    # Guardamos los resultados de la regresion lineal en una clase
    prediction = Predictions(punto_corte_x, m,b, error,bondad, description_var)  #no soy capaz de meter la descripción
    return prediction

def clear_labels():
    '''
    Elimina los elementos de la ventana.
    '''
    global bondad_label, ecuacion_label, error_label, select_x_label,\
        select_x_entry, prediction_button

    # Eliminamos los labels
    if bondad_label is not None:
        bondad_label.config(text="")
    if ecuacion_label is not None:
        ecuacion_label.config(text="")
    if error_label is not None:
        error_label.config(text="")
    if select_x_label is not None:
        select_x_label.config(text="")
    # Eliminamos los entrys y botones
    if prediction_button is not None:
        prediction_button.destroy()
        prediction_button = None
    if select_x_entry is not None:
        select_x_entry.destroy()
        select_x_entry = None

def prediction():
    '''
    Genera una prediccion de y para un valor de x.
    '''
    try:
        x_value = float(select_x_entry.get())       # Valor de x para generar la prediccion de y
        y_prediction = m * x_value + b              # Prediccion de y
        # Modificamos el label de la ecuacion de la recta para mostrar la prediccion de y
        ecuacion_label.config(text=f"Ecuación de la recta: {m:.4f}x + {b:.4f} = {y_prediction:.4f}")
    except ValueError:
        showerror("Error", "El valor de x debe ser un número")
        
def get_description():
    '''
    Devuelve la descripcion actual del modelo.
    '''
    return description.get("1.0", "end-1c") 

def graph(window, x, y, x_title, y_title, y_pred, error):
    '''
    Genera el grafico de regresion lineal y los labels necesarios.
    '''
    global fig, canvas, bondad_label, ecuacion_label, error_label, \
        select_x_entry, prediction_button, select_x_label, description
    
    # Eliminamos los elementos de la ventana que no podemos con clear_labels()
    if 'fig' in globals():
        plt.close(fig)  # Close the previous figure
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

    clear_labels()  # Eliminamos los labels y entrys anteriores   

    # ====================GENERACION DE LABELS====================

    graph_labels = Frame(window)                            # Creamos el frame para los labels
    graph_labels.pack(side=BOTTOM)                          # Posicion del frame

    description = Text(graph_labels, height=3, width=30)    # Create the label for the description
    description.grid(row=0, column=0)                       # Position the label
    description.insert(END, "Descripción: ")                # Insertamos una descripcion
    
    # -------------------ECUACION DE LA RECTA Y BOTON DE PREDICCION-------------------
    ecuacion_label = Label(graph_labels, text=f"Ecuación de la recta: {m:.4f}x + {b:.4f} = y")
    ecuacion_label.grid(row=1, column=0, pady=1, sticky="w")
    prediction_button = Button(graph_labels, text="Predecir", width=15, command=prediction)
    prediction_button.grid(row=1, column=1, pady=1, sticky="w")

    # -------------------VALOR DE X PARA GENERAR LA PREDICCION DE Y-------------------
    select_x_label = Label(graph_labels, text="Valor de x para generar la prediccion de y: ")
    select_x_label.grid(row=2, column=0, pady=1, sticky="w")
    select_x_entry = Entry(graph_labels, width=20)
    select_x_entry.insert(0, x_title)
    select_x_entry.grid(row=2, column=1, pady=1, sticky="w")
    
    # -------------------BONDAD DE AJUSTE Y ERROR COMETIDO-------------------
    bondad_label = Label(graph_labels, text=f"Bondad de ajuste (R^2): {bondad:.4f}")
    bondad_label.grid(row=3, column=0, pady=1, sticky="w")
    
    error_label = Label(graph_labels, text=f"Error cometido: {error}")
    error_label.grid(row=4, column=0, pady=2, sticky="w")

    # ====================GRAFICO====================

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side=LEFT)