import os, pandas, sqlite3
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from pandastable import Table
from MRL_testeo import *

def new_file():
    window.title("Modelo de Regresión Lineal")
    
def open_file():
    '''
    Abre un archivo y devuelve un datagrama con los datos del archivo.
    '''
    global file, data, table
    # Abrimos el explorador de archivos y lo guardamos en file
    file = askopenfilename(defaultextension=".txt",
                            filetypes= [("All Files","*.*"),
                                    ("Excel File","*.xlsx"),
                                    ("CSV File",".csv"),
                                    ("SQL File",".db")])
    if file:
        filepath_label.config(text=file)
        
    file_extension = file.split(".")[-1]                # Cojemos solo la extension
    
    if file_extension == "csv":                         # Si la extension es csv
        data = pandas.read_csv(file)
    
    elif file_extension == "xlsx":                      # Si la extension es xlsx
        data = pandas.read_excel(file)
    
    elif file_extension == "db":                        # Si la extension es db
        conn = sqlite3.connect(file)                    # Abrimos la DB y la asignamos a conn
        data = pandas.read_sql_query\
            ("SELECT * FROM  california_housing_dataset;", conn)  # Cojemos todas las filas
        conn.close()                                    # Cerramos la DB
    
    else:                                               # Si no es ninguno de los anteriores                
        print("No se selecciono un archivo valido o se produjo un error al leerlo.")
        return None                                     # Devolvemos None
    # No necesitamos usar file.close(), askopenfilename ya lo cierra
    return data


def show_columns(data):
    global titulo
    titulo = data.columns                               # Lista con la cabezera del dataframe
    for i in range(len(titulo)):                        # Imprimimos las opciones de columnas
        if data[titulo[i]].dtype == "object":           # Si la columna es de tipo object
            continue
        Label(buttons, text=f"{i}. {titulo[i]}", font=("Consolas",15)).grid(row=i, column=0,sticky="w")

def save_file():
    file = asksaveasfilename(initialfile="untitled.txt",
                                     defaultextension=".txt",
                                     filetypes=[("All Files","*.*"),
                                                 ("Text Docs",".txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file,"w")
                
        except Exception:
            print("not gonna work buddy")
        finally:
            file.close()

def about():
    showinfo("About this progam","This is a progam writen by me :D")

def create():
    x_col = data[titulo[int(variable_x.get())]]
    y_col = data[titulo[int(variable_y.get())]]
    if x_col.equals(y_col):
        showerror("Error", "Las variables no pueden ser iguales")
    x_col_reshaped = x_col.values.reshape(-1, 1)
    y_col_reshaped = y_col.values.reshape(-1, 1)
    mrl_testeo(x_col_reshaped, y_col_reshaped, titulo[int(variable_x.get())], titulo[int(variable_y.get())])
    

# -------------------WINDOW GEOMETRY-------------------

window = Tk()
window.title("Modelo de Regresión Lineal")
file = None

window_height = 720
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

data = open_file()

# FRAME 2
dataframe = Frame(window)
dataframe.pack(side=TOP)

# FRAME 3
buttons = Frame(window)
buttons.pack(side=LEFT, fill=Y)
show_columns(data)
x = IntVar()
y = IntVar()
opciones = [str(i) for i in range(len(titulo))]

variable_x = StringVar(buttons)
variable_x.set("0")  # Default value
xtitle = Label(buttons, text="Variable X: ").grid(row=len(titulo), column=0, sticky="w")
xEntry = OptionMenu(buttons, variable_x, *opciones).grid(row=len(titulo), column=1, sticky="w")

variable_y = StringVar(buttons)
variable_y.set("0")  # Default value
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

# con desplegable
'''opciones = [str(i) for i in range(10)]

variable_x = StringVar(window)
variable_x.set("0")  # Valor por defecto
xtitle = Label(inputs,text="Variable X: ")\
    .grid(row=0, column=0, sticky="w")
xEntry = OptionMenu(inputs, variable_x, *opciones)\
    .grid(row=0, column=1, sticky="w")

variable_y = StringVar(inputs)
variable_y.set("0")  # Valor por defecto
ytitle = Label(inputs,text="Variable Y: ")\
    .grid(row=1, column=0, sticky="w")
yEntry = OptionMenu(inputs, variable_y, *opciones)\
    .grid(row=1, column=1, sticky="w")

createButton = Button(inputs, text= "Create", command=None)\
    .grid(row=2, column=1, sticky="w")'''