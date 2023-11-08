import pandas
from tkinter.filedialog import *
import sqlite3

def open_file():
    '''
    Abre un archivo y devuelve un datagrama con los datos del archivo.
    '''
    # Abrimos el explorador de archivos y lo guardamos en file
    file = askopenfilename(defaultextension=".txt",
                            filetypes= [("All Files","*.*"),
                                    ("Excel File","*.xlsx"),
                                    ("CSV File",".csv"),
                                    ("SQL File",".db")])
    file_extension = file.split(".")[-1]                # Cojemos solo la extension
    
    if file_extension == "csv":                         # Si la extension es csv
        data = pandas.read_csv(file)
        return data                                     # Devolvemos el datagrama CSV
    elif file_extension == "xlsx":                      # Si la extension es xlsx
        data = pandas.read_excel(file)
        return data                                     # Devolvemos el datagrama EXCEL
    elif file_extension == "db":                        # Si la extension es db
        conn = sqlite3.connect(file)                    # Abrimos la DB y la asignamos a conn
        data = pandas.read_sql_query\
            ("SELECT * FROM  california_housing_dataset;", conn)  # Cojemos todas las filas
        conn.close()                                    # Cerramos la DB
        return data                                     # Devolvemos el datagrama DB
    else:                                               # Si no es ninguno de los anteriores                
        print("No se selecciono un archivo valido o se produjo un error al leerlo.")
    # No necesitamos usar file.close(), askopenfilename ya lo cierra