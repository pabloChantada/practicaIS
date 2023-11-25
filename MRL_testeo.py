from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
from predicciones_MRL import *
from tkinter import Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import mean_squared_error
from tkinter.messagebox import showerror
def mrl_testeo(window, x, y, x_title, y_title):
    '''
    Muestra la grafica de dispersion, la regresion lineal, la correlacion y la prediccion de y.
    '''               
    global bondad, m, b, bondad_label, ecuacion_label

    plt.close('all')  # Close all existing figures
    model = LinearRegression().fit(x, y)                                # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                           # Predecimos los valores de y
    x1 = np.reshape(x, -1)                                              # Redimensionamos los valores de x e y para  
    y1 = np.reshape(y, -1)                                              # poder calcular la correlacion, con los vectores 
    m = model.coef_[0][0]
    b = model.intercept_[0]
    punto_corte_x = -b/m
    error = mean_squared_error(y, y_pred)                                                # de una dimension no funciona
    correlation, _ = pearsonr(x1, y1)                                   # normales (1D) no funciona
    bondad = model.score(x, y)            
    graph(window, x, y, x_title, y_title, y_pred, error)                       # Calculamos la bondad de ajuste
    prediction = Predictions(x, y, x_title, y_title, punto_corte_x, m,b, correlation, bondad, description)       #almacenamos las variables y sus correlaciones en una clase
    
    return prediction


bondad_label = None
ecuacion_label = None
error_label = None
selectXEntry = None
selectXVariable = None
yLabel = None
predictionButton = None

def clear_labels():
    global bondad_label, ecuacion_label, error_label, selectXVariable, yLabel,\
        description, selectXEntry, predictionButton
    if bondad_label is not None:
        bondad_label.config(text="")
    if ecuacion_label is not None:
        ecuacion_label.config(text="")
    if error_label is not None:
        error_label.config(text="")
    if selectXVariable is not None:
        selectXVariable.config(text="")
    if yLabel is not None:
        yLabel.config(text="")
    if predictionButton is not None:
        predictionButton.destroy()
        predictionButton = None
    if selectXEntry is not None:
        selectXEntry.destroy()
        selectXEntry = None
    

def graph(window, x, y, x_title, y_title, y_pred, error):
    global fig, canvas, description, bondad_label, ecuacion_label, error_label, selectXVariable, yLabel, predictionButton, selectXEntry
    
    if 'fig' in globals():
        plt.close(fig)  # Close the previous figure

    fig = plt.figure()
    ax = fig.gca()
    ax.scatter(x, y)
    ax.plot(x, y_pred, color='red', linewidth=2, label='Regresión lineal')
    ax.legend()
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_title('Regresión Lineal y Correlación entre X e Y')

    clear_labels()

    # ====================LABELS====================

    graph_labels = Frame(window)
    graph_labels.pack(side=BOTTOM)

    if 'description' in globals() and description is not None:
        description.destroy()

    description = Text(graph_labels, height=3, width=30)
    description.grid(row=0, column=0)
    description.insert("1.0", "Enter description here")  # Add starting text
    
    ecuacion_label = Label(graph_labels, text=f"Ecuación de la recta: {m:.4f}x + {b:.4f} = y")
    ecuacion_label.grid(row=1, column=0, pady=1, sticky="w")
    predictionButton = Button(graph_labels, text="Predecir", width=15, command=prediction)
    predictionButton.grid(row=1, column=1, pady=1, sticky="w")

    selectXVariable = Label(graph_labels, text="Valor de x para generar la prediccion de y: ")
    selectXVariable.grid(row=2, column=0, pady=1, sticky="w")
    selectXEntry = Entry(graph_labels, width=20)
    selectXEntry.insert(0, x_title)
    selectXEntry.grid(row=2, column=1, pady=1, sticky="w")
    
    bondad_label = Label(graph_labels, text=f"Bondad de ajuste (R^2): {bondad:.4f}")
    bondad_label.grid(row=3, column=0, pady=1, sticky="w")
    
    error_label = Label(graph_labels, text=f"Error cometido: {error}")
    error_label.grid(row=4, column=0, pady=2, sticky="w")

    # ====================GRAFICO====================
    if 'canvas' in globals() and canvas is not None:
        canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side=LEFT)

def prediction():
    try:
        x_value = float(selectXEntry.get())
        y_value = m * x_value + b 
        ecuacion_label.config(text=f"Ecuación de la recta: {m:.4f}x + {b:.4f} = {y_value:.4f}")
    except ValueError:
        showerror("Error", "El valor de x debe ser un número")