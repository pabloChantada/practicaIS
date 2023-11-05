import file_reader
import MRL_testeo

def show_columns(data, var):
    titulo = data.columns                               # Lista con la cabezera del dataframe
    print('NOMBRE DE LAS COLUMNAS:')
    for i in range(len(titulo)):                        # Imprimimos las opciones de columnas
        print(f"{i}. {titulo[i]}")
        # SE PUEDE REPETIR COLUMNA? PREGUNTAR
    while True:                                         # Repetimos el bucle hasta que se seleccione una columna valida                              
        try:
            var_selection = int(input(f'\nSeleccione el nombre de la columna para la variable {var}: '))
            if var_selection < 0:                       # Caso de variables negativas
                print('\nNo se aceptan columnas negativas.')
                continue
            selection = data[[titulo[var_selection]]]   # Cojemos del df la columna de la cabezera(titulo) seleccionada
            return selection                            # Devolvemos la columna seleccionada
        except (IndexError, ValueError):                # Caso de variables no numericas
            print('\nSeleccione un numero valido')
                
data = file_reader.open_file()                          # Abrimos el archivo y lo guardamos en data
print(data)                                             # Mostramos el dataframe al usuario
x = show_columns(data, 'x')                             # SELECCION DE VARIABLE X
y = show_columns(data, 'y')                             # SELECCION DE VARIABLE Y
print("Variable X seleccionada: ",x)                    # Mostramos la variable x
print("Variable Y seleccionada: ",y)                    # Mostramos la variable y
x_title = x.columns[0]                                  # Mostramos el titulo de la variable x
y_title = y.columns[0]                                  # Mostramos el titulo de la variable y
MRL_testeo.mrl_testeo(x, y, x_title, y_title)           # Mostramos el MRL