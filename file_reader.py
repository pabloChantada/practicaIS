import pandas
from tkinter.filedialog import *

def open_file():
    # Abrimos los archivos con filedialog y ensenamos .csv, .xlsx, y all files
    file = askopenfilename(defaultextension=".txt",
                            filetypes= [("All Files","*.*"),
                                    ("Excel File","*.xlsx"),
                                    ("CSV File",".csv")])
    file_extension = file.split(".")[-1]  # Cojemos solo la extension
    # Lectura de CSV
    if file_extension == "csv":
        data = pandas.read_csv(file)
        return data  # Devolvemos el datagrama
    # Lectura de EXCEL
    elif file_extension == "xlsx":
        data = pandas.read_excel(file)
        return data  # Devolvemos el datagrama
    elif file_extension == 3:
        # Añadir sql
        '''
        data = sql_reader.data()        
        conn = sqlite3.connect('example.db')
        data = pd.read_sql_query("SELECT * FROM table_name;", conn)
        conn.close()
        '''
        pass
    # No necesitamos usar file.close(), askopenfilename ya lo cierra
