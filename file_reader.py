import pandas
from tkinter.filedialog import *

def open_file():
    file = askopenfilename(defaultextension=".txt",
                                          file= [("All Files","*.*"),
                                                 ("Excel File","*.xlsx"),
                                                 ("CSV File",".csv")])
    file_extension = file.split(".")[-1]
    if file_extension == "csv":
        data = pandas.read_csv(file)
        return data
    elif file_extension == "xlsx":
        data = pandas.read_excel(file)
        return data
    elif file_extension == 3:
        # añadir sql
        '''
        data = sql_reader.data()        
        conn = sqlite3.connect('example.db')
        data = pd.read_sql_query("SELECT * FROM table_name;", conn)
        conn.close()
        '''
        pass

    # file.close()