import pandas
from tkinter.filedialog import *
import sqlite3

def open_file():
    # Abrimos los archivos con filedialog y enseñamos .csv, .xlsx, .db y all files
    file = askopenfilename(defaultextension=".txt",
                            filetypes= [("All Files","*.*"),
                                    ("Excel File","*.xlsx"),
                                    ("CSV File",".csv"),
                                    ("SQL File",".db")])
    file_extension = file.split(".")[-1]  # Cojemos solo la extension
    # Lectura de CSV
    if file_extension == "csv":
        data = pandas.read_csv(file)
        return data  # Devolvemos el datagrama
    # Lectura de EXCEL
    elif file_extension == "xlsx":
        data = pandas.read_excel(file)
        return data  # Devolvemos el datagrama
    # Lectura de DB
    elif file_extension == "db":
        conn = sqlite3.connect(file)  # Abrimos la DB y la asignamos a conn
        data = pandas.read_sql_query("SELECT * FROM  california_housing_dataset;", conn)  # Cojemos todas las filas
        conn.close()  # Cerramos la DB
        return data  # Devolvemos el datagrama
    # En caso de que no se seleccione nada o no sea un csv, xlsx o db mostraos un error
    else:
        print("No se selecciono un archivo valido o se produjo un error al leerlo.")
    #  No necesitamos usar file.close(), askopenfilename ya lo cierra