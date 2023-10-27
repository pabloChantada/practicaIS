import file_reader

def show_columns(data):
    titulo = data.columns
    for i in range(len(titulo)):
        print(f"{i}. {titulo[i]}")
    var_selection = int(input('\nSeleccione el nombre de la columna para la variable x: '))
    selection = data[titulo[var_selection]]
    return selection

data = file_reader.open_file()
print(data)
show = show_columns(data)
while True:
    try:
        x = show_columns(data)
        y = show_columns(data)
    except ValueError:
        print('Seleccione un nombre valido')

print(f'Varible x: {x_selection}')
print(x,'\n')
print(f'Varible y: {y_selection}')
print(y)