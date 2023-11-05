import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Crea un modelo de regresión lineal
model = LinearRegression()
model.fit(X, Y)

# Realizamos las predicciones
Y_pred = model.predict(X)

# Calcular la correlación entre X e Y
correlation, _ = pearsonr(data[columna_x], data[columna_y])

# Imprime la correlación entre X e Y.
print(f"Correlación entre {columna_x} y {columna_y}: {correlation:.2f}")

# Visualización de los resultados en una gráficoa.
plt.scatter(data[columna_x], data[columna_y], label='Datos reales')
plt.plot(data[columna_x], Y_pred, color='red', linewidth=2, label='Regresión lineal')
plt.xlabel(columna_x)
plt.ylabel(columna_y)
plt.legend()
plt.title('Regresión Lineal y Correlación entre X e Y')
plt.show()
