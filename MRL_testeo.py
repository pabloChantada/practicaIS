from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

def mrl_testeo(x, y, x_title, y_title):
    '''
    Muestra la grafica de dispersion, la regresion lineal, la correlacion y la prediccion de y.
    '''                                 
    model = LinearRegression().fit(x, y)                                # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                           # Predecimos los valores de y
    x1 = np.reshape(x, -1)                                              # Redimensionamos los valores de x e y para  
    y1 = np.reshape(y, -1)                                              # poder calcular la correlacion, con los vectores                                           
    correlation, _ = pearsonr(x1, y1)                                   # normales (1D) no funciona
    
    # mostrar con un alerta la correlacion y la bondad de ajuste
    print(f"Correlación entre {x_title} e {y_title}: {correlation}")    # Mostramos la correlacion
    print("Variable x: \n",x)                                           # Mostramos los valores de x
    print("Variable y: \n",y)                                           # Mostramos los valores de y
    print("Bondad de ajuste: ",model.score(x, y) )                      # Mostramos la bondad de ajuste
    print("Predicción de y: \n",y_pred)                                 # Mostramos la prediccion de y

    plt.scatter(x, y)                                                   # Mostramos la grafica de dispersion
    plt.plot(x, y_pred, color='red', 
                                linewidth=2, 
                                label='Regresión lineal')               # Mostramos la regresion lineal
    plt.xlabel('VARIABLE X')                                            # Mostramos los titulo del eje x
    plt.ylabel('VARIABLE Y')                                            # Mostramos los titulo del eje y
    plt.legend()                                                        # Mostramos la leyenda
    plt.title('Regresión Lineal y Correlación entre X e Y')             # Titulo de la grafica
    plt.show()                                                          # Mostramos la grafica                                            