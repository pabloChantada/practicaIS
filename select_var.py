import file_reader

def show_columns(data, var = None):
    titulo = data.columns  # Lista con la cabezera del dataframe
    # Imprimimos el indice y la columna
    for i in range(len(titulo)):
        print(f"{i}. {titulo[i]}")
    # Anadimos esta condicion en caso de que solo queramos imprimnir las columnas
    if var is not None:
        # SE PUEDE REPETIR COLUMNA? PREGUNTAR
        while True:
            try:
                var_selection = int(input(f'\nSeleccione el nombre de la columna para la variable {var}: '))
                selection = data[titulo[var_selection]]  # Cojemos del df la columna de la cabezera(titulo) seleccionada
                return selection
            except (IndexError, ValueError, var_selection < 0):
                print('\nSeleccione un numero valido')
                
# Abirmos el archivo y lo almacenamos en data
data = file_reader.open_file()
print(data)  # Mostramos el df al usuario

print('\nNOMBRE DE LAS COLUMNAS:')
x = show_columns(data, 'x')  # SELECCION DE VARIABLE X
y = show_columns(data, 'y')  # SELECCION DE VARIABLE Y
# Mostramos las variables
print('\nLa variable x seleccionada es: ', x)
print('\nLa variable y seleccionada es: ', y)
