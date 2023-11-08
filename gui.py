import os, file_reader
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from select_var import show_columns
from MRL_testeo import mrl_testeo

def new_file():
    window.title("Modelo de Regresión Lineal")

def executable():
    data = file_reader.open_file()                          # Abrimos el archivo y lo guardamos en data
    print(data)                                             # Mostramos el dataframe al usuario

    x = show_columns(data, 'x')                             # SELECCION DE VARIABLE X
    y = show_columns(data, 'y')                             # SELECCION DE VARIABLE Y
    print("Variable X seleccionada: ",x)                    # Mostramos la variable x
    print("Variable Y seleccionada: ",y)                    # Mostramos la variable y

    x_title = x.columns[0]                                  # Mostramos el titulo de la variable x
    y_title = y.columns[0]                                  # Mostramos el titulo de la variable y
    mrl_testeo(x, y, x_title, y_title)                      # Mostramos el MRL

def create():
    mrl_testeo(xEntry, yEntry, "x", "y")


def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
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

# -------------------WINDOW GEOMETRY-------------------
window = Tk()
window.title("Modelo de Regresión Lineal")
file = None

window_height = 720
window_width = 720
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/ 2) - (window_width / 2))
y = int((screen_height/ 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# -------------------TEXT AREA-------------------

xtitle = Label(window,text="Variable X: ").grid(row=0,column=0)
xEntry = Entry(window).grid(row=0,column=1)

xtitle = Label(window,text="Variable X: ").grid(row=1,column=0)
yEntry = Entry(window).grid(row=1,column=1)

createButton = Button(window, text= "Create", command=create).grid(row=3,column=0 , columnspan=2)

# -------------------MENU-------------------

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=  0)
menubar.add_cascade(label="File",menu= fileMenu)
fileMenu.add_command(label="New file",command= new_file)
fileMenu.add_command(label="Open file",command= executable)
fileMenu.add_command(label="Save file",command= save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command= quit)

helpMenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label="Help",menu= helpMenu)
helpMenu.add_command(label="About",command= about)

window.mainloop()