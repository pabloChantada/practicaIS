import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sqlalchemy import create_engine

# Opción para elegir la fuente de datos (1:CSV, 2:Excel o 3:Base de datos)

opcion_fuente = '2'

if opcion_fuente == '1':
    # Cargar datos desde un archivo CSV y elegir las columnas X e Y
    archivo_csv = 'housing.csv'
    columna_x = 'longitude'         #ejemplo  ////HAY QUE IMPLEMENTAR EL SELECT_VAR
    columna_y = 'latitude'          #ejemplo  ////HAY QUE IMPLEMENTAR EL SELECT_VAR

    data = pd.read_csv(archivo_csv)
    X = data[[columna_x]]
    Y = data[[columna_y]]
    
elif opcion_fuente == '2':
    # Cargar datos desde un archivo Excel y elegir las columnas X e Y
    archivo_excel = 'housing.xlsx'
    hoja_excel = 'housing'
    columna_x = 'longitude'             #ejemplo  ////HAY QUE IMPLEMENTAR EL SELECT_VAR
    columna_y = 'latitude'              #ejemplo ////HAY QUE IMPLEMENTAR EL SELECT_VAR

    data = pd.read_excel(archivo_excel, sheet_name=hoja_excel)
    X = data[[columna_x]]
    Y = data[[columna_y]]
    
elif opcion_fuente == '3':              
    # Conectar a la base de datos y elegir las columnas X e Y
    ruta_basededatos = 'sqlite:///tu_basededatos.db'    # Poner nuestra Base de datos
    tabla = 'nombre_de_la_tabla'                        #Poner nuestra tabla de la base de datos
    columna_x = 'poner nombre col x'                    #Elegimos los nombres de las columnas x e y////HAY QUE IMPLEMENTAR SELECT_VAR
    columna_y = 'poner nombre col y'              

    engine = create_engine(ruta_basededatos)
    query = f"SELECT {columna_x}, {columna_y} FROM {tabla}"

    data = pd.read_sql(query, engine)
    X = data[[columna_x]]
    Y = data[[columna_y]]
    
else:
    print("Opción no válida. Debes elegir 1, 2 o 3 para la fuente de datos.")
    exit()

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





