import pandas
from tkinter.filedialog import *
import sqlite3
def open_file():
    # Abrimos los archivos con filedialog y ensenamos .csv, .xlsx, y all files
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
    elif file_extension == "db":
    # LECTURA DE SQL
        #data = sql_reader.data()        
        conn = sqlite3.connect('housing.db')
        data = pandas.read_sql_query("SELECT * FROM  california_housing_dataset;", conn)
        conn.close()
        return data
        
    # No necesitamos usar file.close(), askopenfilename ya lo cierra

result = open_file()

if result is not None:
    print("Datos leidos con exito:")
    print(result)
else:
    print("No se selecciono un archivo valido o se produjo un error al leerlo.")