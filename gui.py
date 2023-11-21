import os, pandas, sqlite3
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from pandastable import Table
from MRL_testeo import *
from predicciones_MRL import Predictions
import pickle

def new_file():
    window.title("Modelo de Regresión Lineal")
    
def open_file(file=None):
    '''
    Abre un archivo y devuelve un datagrama con los datos del archivo.
    '''
    global data, table, filepath_label
    # Abrimos el explorador de archivos y lo guardamos en file
    if file == None:
        file = askopenfilename(defaultextension=".txt",
                                filetypes= [("All Files","*.*"),
                                        ("Excel File","*.xlsx"),
                                        ("CSV File",".csv"),
                                        ("SQL File",".db"),
                                        ("Pickle File",".plk")])
    else:
        file = file
    if file:
        filepath_label.config(text=file)
        
    file_extension = file.split(".")[-1]                # Cojemos solo la extension
    match file_extension:                               # Comparamos la extension
        case "csv":                                     # Si la extension es csv
            data = pandas.read_csv(file)
        
        case "xlsx":                                    # Si la extension es xlsx
            data = pandas.read_excel(file)
        
        case "db":                                      # Si la extension es db
            conn = sqlite3.connect(file)                    # Abrimos la DB y la asignamos a conn
            data = pandas.read_sql_query("SELECT * FROM  california_housing_dataset;", conn)  # Cojemos todas las filas
            conn.close()                                    # Cerramos la DB
        case "pkl":
            # Función para cargar las predicciones desde el archivo usando pickle
            Predictions.load_file(window, file)
        case _:           
            print("No se selecciono un archivo valido o se produjo un error al leerlo.")
            return None                                     # Devolvemos None
    if file_extension != "pkl":
        # Eliminar filas con Nan
        data = data.dropna() 
        return data


def save_file():
    file = asksaveasfilename(initialfile="prediction.pkl",
                             defaultextension=".pkl",
                             filetypes=[("Pickle Files",".pkl")])
    if file:
        if os.path.exists(file):                     #si ya existe el archivo predicciones.plk
            with open(file, 'ab') as file:           #abrimos el archivo en modo binario para añadir 
                pickle.dump(prediction, file)           #las predicciones al final del archivo

        else:                                           #si no existe el archivo predicciones.plk         
            with open(file, 'wb') as file:           #creamos un archivo en modo binario
                pickle.dump(prediction, file)           #para escribir la primera prediccion    

def about():
    showinfo("About this progam","This is a progam writen by me :D")

def create():
    global prediction
    x_col = data[variable_x.get()]
    y_col = data[variable_y.get()]
    if x_col.equals(y_col):
        showerror("Error", "Las variables no pueden ser iguales")
    else:
        x_col_reshaped = x_col.values.reshape(-1, 1)
        y_col_reshaped = y_col.values.reshape(-1, 1)
        prediction = mrl_testeo(window, x_col_reshaped, y_col_reshaped, variable_x.get(), variable_y.get())        
        

# -------------------WINDOW GEOMETRY-------------------

window = Tk()
window.title("Modelo de Regresión Lineal")
file = None

window_height = 780
window_width = 950
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/ 2) - (window_width / 2))
y = int((screen_height/ 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
window.resizable(False, False)

# -------------------TEXT AREA-------------------

# FRAME 1
inputs = Frame(window)
inputs.pack(side=BOTTOM, fill=X)

path = Label(inputs, text="File Path: ")
path.grid(row=4, column=0, sticky="w")
filepath_label = Label(inputs, text="")
filepath_label.grid(row=4, column=1, sticky="w")

# FRAME 2
dataframe = Frame(window)
dataframe.pack(side=TOP)

# FRAME 3
buttons = Frame(window)
buttons.pack(side=LEFT, fill=Y)

data = open_file('databases\\housing.csv')
titulo = data.columns
# opciones = [i for i in titulo if not isinstance(data[i], str)]
opciones = []
for i in titulo:
    if not isinstance(data[i][1], str):
        opciones.append(i)
        
variable_x = StringVar(buttons)
variable_x.set("Seleccionar")  # Default value
xtitle = Label(buttons, text="Variable X: ").grid(row=len(titulo), column=0, sticky="w")
xEntry = OptionMenu(buttons, variable_x, *opciones).grid(row=len(titulo), column=1, sticky="w")

variable_y = StringVar(buttons)
variable_y.set("Seleccionar")  # Default value
ytitle = Label(buttons, text="Variable Y: ").grid(row=len(titulo) + 1, column=0, sticky="w")
yEntry = OptionMenu(buttons, variable_y, *opciones).grid(row=len(titulo) + 1, column=1, sticky="w")

createButton = Button(buttons, text="Create", command=create).grid(row=len(titulo) + 2, column=0, sticky="w")

table = Table(dataframe, width=window_width, dataframe=data, rows=5)
table.show()

# Add a new row to the dataframe frame

# -------------------MENU-------------------

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New file", command=new_file)
fileMenu.add_command(label="Open file", command=open_file)
fileMenu.add_command(label="Save file", command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
ytitle = Label(buttons, text="Variable Y: ").grid(row=len(titulo) + 1, column=0, sticky="w")
yEntry = OptionMenu(buttons, variable_y, *opciones).grid(row=len(titulo) + 1, column=1, sticky="w")

createButton = Button(buttons, text= "Create", command=create).grid(row=len(titulo) + 2, column=0, sticky="w")

table = Table(dataframe, width=window_width, dataframe=data, rows=5)
table.show()

# Add a new row to the dataframe frame

# -------------------MENU-------------------

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New file", command=new_file)
fileMenu.add_command(label="Open file", command=open_file)
fileMenu.add_command(label="Save file", command=save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=about)

# -------------------FILEPATH LABEL-------------------

window.mainloop()
