import pandas
from tkinter.filedialog import *

def open_file():
    # abrimos los archivos con filedialog y ensenamos .csv, .xlsx,y all files
    file = askopenfilename(defaultextension=".txt",
                            filetypes= [("All Files","*.*"),
                                    ("Excel File","*.xlsx"),
                                    ("CSV File",".csv")])
    file_extension = file.split(".")[-1] # cojemos solo la extension
    # lectura de CSV
    if file_extension == "csv":
        data = pandas.read_csv(file)
        return data # devolvemos el datagrama
    # lectura de EXCEL
    elif file_extension == "xlsx":
        data = pandas.read_excel(file)
        return data # devolvemos el datagrama
    elif file_extension == 3:
        # añadir sql
        '''
        data = sql_reader.data()        
        conn = sqlite3.connect('example.db')
        data = pd.read_sql_query("SELECT * FROM table_name;", conn)
        conn.close()
        '''
        pass
    # no necesitamos usar file.close(), askopenfilename ya lo cierra