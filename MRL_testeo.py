from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
from tkinter.messagebox import showinfo

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
