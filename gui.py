import pandas, sqlite3, pickle, sys, MRL_testeo
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from pandastable import Table
from MRL_testeo import modelo_regresion_lineal as mrl
from predicciones_MRL import generate_labels_prediction

# ===================MENU SUPERIOR===================

def open_file():
    '''
    Abre un archivo y devuelve un datagrama con los datos del archivo.
    '''
    global data, table, file_path_label, file_open
    
    file_open = askopenfilename(defaultextension=".txt",        # Abrimos el explorador de archivos
                            filetypes= [("All Files","*.*"),    # y mostramos los archivos que se 
                                    ("Excel File","*.xlsx"),    # pueden abrir
                                    ("CSV File",".csv"),
                                    ("SQL File",".db")])        
    file_extension = file_open.split(".")[-1]                   # Cojemos solo la extension
    
    match file_extension:                                       # Comparamos la extension
        case "csv":                                             # Si la extension es csv
            data = pandas.read_csv(file_open)
        case "xlsx":                                            # Si la extension es xlsx
            data = pandas.read_excel(file_open)
        case "db":                                              # Si la extension es db
            conn = sqlite3.connect(file_open)                   # Abrimos la DB

            # Cojemos todas las filas de la tabla california_housing_dataset
            data = pandas.read_sql_query("SELECT * FROM  california_housing_dataset;", conn)
            conn.close()                                        # Cerramos la DB
        case "pkl":
            show_file_path(file_open)                           # Mostramos la ruta del archivo
            load_model()                                        # Cargamos el archivo pickle
        case _:                                                 # Caso de fallo                         
            showerror("Error al abrir el archivo",\
                    "No se selecciono un archivo valido o se produjo un error al leerlo.")
            return None                             
        
    if file_extension != "pkl":                         # Si la extension no es pkl (tiene su propia carga de datos)
        for widget in window.winfo_children():          # Eliminamos los widgets de la ventana
            if widget != menu_bar:
                widget.destroy()
        data = data.dropna()                            # Eliminamos los valores nulos       
        dataframe(data)                                 # Generamos el dataframe
        show_file_path(file_open)                       # Mostramos la ruta del archivo
        generate_var(data)                              # Generamos las variables



def save_file():
    '''
    Guarda un archivo en formato pickle.
    '''
    try:
        prediction.description = MRL_testeo.get_description()               # Guardamos la descripcion
        
        file = asksaveasfilename(initialfile="prediction.pkl",              # Mostramos el explorador de archivos
                                defaultextension=".pkl",
                                filetypes=[("Pickle Files",".pkl")])

        if file:                                                            # Si el archivo ya existe
            with open(file, 'wb') as f:                                     # Abriremos el archivo en modo escritura binaria
                pickle.dump(prediction, f)                                  # Guardamos el objeto en el archivo
    except Exception as e:
        showerror("Error", "Error al guardar el archivo: " + str(e))

def clear_gui():

    for widget in window.winfo_children():
        if widget != menu_bar:
            widget.destroy()

def load_model():
    file = askopenfilename(defaultextension=".txt", filetypes=[("Pickle File", ".pkl")])

    with open(file, 'rb') as f:
        try:
            prediction = pickle.load(f)
            clear_gui()
            show_file_path(file)
            generate_labels_prediction(window, prediction)

        except EOFError:
            showerror("Error", "Error al seleccionar el archivo")

# Mostramos un mensaje con los autores
def about():
    showinfo("Autores", "Pablo Chantada Saborido\n"        
                        "Pablo Verdes Sánchez\n"
                        "Claudia Vidal\n"
                        "Aldana Medyna\n"
                        "Ana Valls")

# ===================CREADOR DE MODELOS===================

def create():
    '''
    Crea el modelo de regresion lineal.
    '''
    global prediction                                                   # Hacemos la variable global para poder guardarla
    if variable_x.get() == 'Select' or variable_y.get() == 'Select':    # Comprobamos que no haya valores nulos
        showerror("Error", "No se pueden introducir valores nulos")
        
    else:
        x_col = data[variable_x.get()]          # Cojemos la columna de la variable x
        y_col = data[variable_y.get()]          # Cojemos la columna de la variable y
        if x_col.equals(y_col):                 # Comprobamos que las variables no sean iguales       
            showerror("Error", "Las variables no pueden ser iguales")

        else:
            x_col_reshaped = x_col.values.reshape(-1, 1)  # Redimensionamos los valores de x
            y_col_reshaped = y_col.values.reshape(-1, 1)  # Redimensionamos los valores de y

            # Guardamos el resultado de la funcion mrl_testeo en la variable prediction
            prediction = mrl(window, x_col_reshaped, y_col_reshaped, variable_x.get(), variable_y.get())        

def generate_var(data):
    '''
    Genera las variables que empleará el modelo de regresión lineal

    Parametros:
    --------------

    data: Dataframe sin valores nulos
    '''
    global variable_x, variable_y
    # -------------------BOTONES-------------------
    buttons = Frame(window)                             # Creamos el frame para los botones 
    buttons.pack(side=LEFT, fill=Y)                     # Posicion del frame

    titulo = data.columns                               # Cojemos los titulos de las columnas

    #Esto lo quitamos??:
    # opciones = [i for i in titulo if not isinstance(data[i], str)]

    opciones = []                                       # Lista para guardar las opciones de las variables
    for i in titulo:
        if not isinstance(data[i][1], str):             # Evitamos las columnas con strings
            opciones.append(i)

    # -------------------VARIABLE X-------------------
    variable_x = StringVar(buttons)                     # Creamos la variable de strings para la variable x
    variable_x.set("Select")                            # Valor por defecto
    x_title = Label(buttons, text="Variable X: ").\
        grid(row=0, column=0, sticky="w")
    x_entry = OptionMenu(buttons, variable_x, *opciones).\
        grid(row=0, column=1, sticky="w")

    # -------------------VARIABLE Y-------------------
    variable_y = StringVar(buttons)                     # Creamos la variable de strings para la variable y
    variable_y.set("Select")  # Default value           # Valor por defecto
    y_title = Label(buttons, text="Variable Y: ").\
        grid(row=0, column=2, sticky="w")
    y_entry = OptionMenu(buttons, variable_y, *opciones).\
    grid(row=0, column=3, sticky="w")
    
    # -------------------BOTON CREAR-------------------
    create_button = Button(buttons, text="Crear modelo", command=create).\
    grid(row=2, column=0, sticky="w")
    
def dataframe(data):
    '''
    Muestra el Dataframe
    
    Parametros:
    --------------

    data: Dataframe sin valores nulos
    '''
    # -------------------DATAFRAME-------------------

    dataframe = Frame(window)                           # Creamos el frame para el dataframe
    dataframe.pack(side=TOP)                            # Posicion del frame   
    # Creamos la tabla con el dataframe
    table = Table(dataframe, width=window_width, dataframe=data)
    table.show()

def show_file_path(file_open):
    '''
    Muestra la ruta del archivo abierto.
    
    Parametros:
    --------------

    file_open: Archivo que se abre
    '''
    file_path_frame = Frame(window)                     # Creamos el frame para la ruta del archivo
    file_path_frame.pack(side=BOTTOM, anchor="sw")      # Posicion del frame en la esquina inferior izquierda
    file_path_label = Label(file_path_frame, text=f"File Path: {file_open}") 
    file_path_label.pack(side=LEFT)                     # Posicion del label a la izquierda
    
# ===================GEOMETRIA DE LA VENTANA===================

window = Tk()                                           # Creamos la ventana

window.title("Modelo de Regresión Lineal")              # Titulo de la ventana

window_height = 850                                     # Altura de la ventana
window_width = 1000                                     # Ancho de la ventana
screen_height = window.winfo_screenheight()             # Alto de la pantalla
screen_width = window.winfo_screenwidth()               # Largo de la pantalla
x = int((screen_width/ 2) - (window_width / 2))         # Ajustamos la coordenada x a la pantalla
y = int((screen_height/ 2.15) - (window_height / 2))    # Ajustamos la coordenada y a la pantalla

# Ajustamos la geometria de la ventana
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))    
window.resizable(False, False)                          # Hacemos que la ventana no se pueda redimensionar

# ===================MENU SUPERIOR COMANDOS===================

menu_bar = Menu(window)                                      # Creamos la barra de menu
window.config(menu=menu_bar)                                 # Añadimos la barra de menu a la ventana
file_menu = Menu(menu_bar, tearoff=0)                        # Creamos el menu de archivo
menu_bar.add_cascade(label="File", menu=file_menu)           # Añadimos el menu de archivo a la barra de menu
file_menu.add_command(label="Open file", command=open_file)  # Añadimos la opcion de abrir archivo al menu de archivo
file_menu.add_command(label="Save file", command=save_file)  # Añadimos la opcion de guardar archivo al menu de archivo
file_menu.add_command(label="Load model", command=load_model)
file_menu.add_separator()                                    # Añadimos una separacion al menu de archivo
file_menu.add_command(label="Exit", command=sys.exit)        # Añadimos la opcion de salir al menu de archivo

help_menu = Menu(menu_bar, tearoff=0)                        # Creamos el menu de ayuda
menu_bar.add_cascade(label="Help", menu=help_menu)           # Añadimos el menu de ayuda a la barra de menu
help_menu.add_command(label="About", command=about)          # Añadimos la opcion de about al menu de ayuda

window.protocol("WM_DELETE_WINDOW", sys.exit)                # Cerramos la ventana al pulsar la X
window.mainloop()                                            # Bucle principal de la ventana