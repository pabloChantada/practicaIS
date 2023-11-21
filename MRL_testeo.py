from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
from PIL import Image, ImageTk
from predicciones_MRL import *
from tkinter import Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
    correlation, _ = pearsonr(x1, y1)                                   # normales (1D) no funciona
    bondad = model.score(x, y)                                          # Calculamos la bondad de ajuste
    prediction = Predictions(x, y, x_title, y_title, punto_corte_x, m,b, correlation, bondad)       #almacenamos las variables y sus correlaciones en una clase
    graph(window, x, y, x_title, y_title, y_pred)
    
    return prediction, bondad, m, b

bondad_label = None
ecuacion_label = None

def graph(window, x, y, x_title, y_title, y_pred):
    global fig, canvas, bondad_label, ecuacion_label

    if 'fig' in globals():
        plt.close(fig)  # Close the previous figure

    fig = plt.figure()
    ax = fig.gca()
    ax.scatter(x, y)
    ax.plot(x, y_pred, color='red', linewidth=2, label='Regresión lineal')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.legend()
    ax.set_title('Regresión Lineal y Correlación entre X e Y')

    if bondad_label is not None and bondad_label.winfo_exists() and \
        ecuacion_label is not None and ecuacion_label.winfo_exists():
        bondad_label.destroy()
        ecuacion_label.destroy()

    bondad_label = Label(window, text=f"Bondad de ajuste: {bondad:.4f}")
    bondad_label.pack(side=BOTTOM)
    ecuacion_label = Label(window, text=f"Ecuación de la recta: y = {m:.4f}x + {b:.4f}")
    ecuacion_label.pack(side=BOTTOM)

    if 'canvas' in globals() and canvas.get_tk_widget().winfo_exists():
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)