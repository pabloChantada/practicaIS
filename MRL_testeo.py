from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

def mrl_testeo(x, y, x_title, y_title):                                 # Funcion que muestra el MRL, correlacion
    model = LinearRegression().fit(x, y)                                # Creamos el modelo de regresion lineal 
    y_pred = model.predict(x)                                           # Predecimos los valores de y
    x1 = np.reshape(x, -1)                                              # Redimensionamos los valores de x e y para  
    y1 = np.reshape(y, -1)                                              # poder calcular la correlacion, con los vectores                                           
    correlation, _ = pearsonr(x1, y1)                                   # normales (1D) no funciona
    print(f"Correlación entre {x_title} e {y_title}: {correlation}")    # Mostramos la correlacion
    # print(f"Coeficiente de la pendiente: {model.coef_[0][0]}")
    # print(f"Coeficiente de la intercepcion: {model.intercept_[0]}")
    print("Variable x: \n",x)
    print("Variable y: \n",y)
    print("Bondad de ajuste: ",model.score(x, y) )
    print("Predicción de y: \n",y_pred)
    # Graficamos los valores de x e y, y la regresion lineal
    plt.scatter(x, y)
    plt.plot(x, y_pred, color='red', 
                                linewidth=2, 
                                label='Regresión lineal')
    plt.xlabel('VARIABLE X')
    plt.ylabel('VARIABLE Y')
    plt.legend()
    plt.title('Regresión Lineal y Correlación entre X e Y')
    plt.show() 