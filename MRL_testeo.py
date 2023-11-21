from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
from tkinter.messagebox import showinfo
from predicciones_MRL import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Label

def mrl_testeo(x, y, x_title, y_title):
    '''
    Muestra la grafica de dispersion, la regresion lineal, la correlacion y la prediccion de y.
    '''               
    model = LinearRegression().fit(x, y)                                # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                           # Predecimos los valores de y
    x1 = np.reshape(x, -1)                                              # Redimensionamos los valores de x e y para  
    y1 = np.reshape(y, -1)                                              # poder calcular la correlacion, con los vectores                                           
    correlation, _ = pearsonr(x1, y1)                                   # normales (1D) no funciona
    bondad = model.score(x, y)                                          # Calculamos la bondad de ajuste
    prediction = Predictions(x, y, x_title, y_title, correlation, bondad)       #almacenamos las variables y sus correlaciones en una clase
    reult_str = f"Bondad de ajuste: {bondad}\
        \nCorrelación entre {x_title} e {y_title}: {correlation}"

    plt.scatter(x, y)                                                   # Mostramos la grafica de dispersion
    plt.plot(x, y_pred, color='red', 
                                linewidth=2, 
                                label='Regresión lineal')               # Mostramos la regresion lineal
    plt.xlabel('VARIABLE X')                                            # Mostramos los titulo del eje x
    plt.ylabel('VARIABLE Y')                                            # Mostramos los titulo del eje y
    plt.legend()                                                        # Mostramos la leyenda
    plt.title('Regresión Lineal y Correlación entre X e Y')             # Titulo de la grafica
    plt.show()                                                          # Mostramos la grafica
    showinfo("Resultados", reult_str)   # Mostramos los resultados en una ventana de mensaje
    return prediction

def mrl_testeo_gui(window, x, y, x_title, y_title):

    model = LinearRegression().fit(x, y)                                # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                           # Predecimos los valores de y
    x1 = np.reshape(x, -1)                                              # Redimensionamos los valores de x e y para  
    y1 = np.reshape(y, -1)                                              # poder calcular la correlacion, con los vectores                                           
    correlation, _ = pearsonr(x1, y1)                                   # normales (1D) no funciona
    bondad = model.score(x, y)                                          # Calculamos la bondad de ajuste
    #prediction = Predictions(x, y, x_title, y_title, correlation, bondad)       #almacenamos las variables y sus correlaciones en una clase
    #reult_str = f"Bondad de ajuste: {bondad}\
    #    \nCorrelación entre {x_title} e {y_title}: {correlation}"
    
    m = model.coef_[0][0]
    b = model.intercept_[0]

    # Creamos una figura de Matplotlib e incrustamos en la ventana de Tkinter
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.plot(x, y_pred, color='red', linewidth=2, label='Regresión lineal')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.legend()
    ax.set_title('Regresión Lineal y Correlación entre X e Y')
    
 # Mostramos la bondad de ajuste en algún lugar de la interfaz gráfica

    bondad_label = Label(window, text=f"Bondad de ajuste: {bondad:.4f}")
    bondad_label.pack(side=BOTTOM)  # Ajusta esto según tu diseño

 # Muestra la ecuación de la recta en algún lugar de la interfaz gráfica
    ecuacion_label = Label(window, text=f"Ecuación de la recta: y = {m:.4f}x + {b:.4f}")
    ecuacion_label.pack(side=BOTTOM)  # Ajusta esto según tu diseño


    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=TOP, fill=BOTH, expand=1)
    return prediction
