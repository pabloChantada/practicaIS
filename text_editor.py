import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def new_file():
    window.title("Untitle")
    text.delete("1.0",END)

def open_file():
    file = askopenfilename(defaultextension=".txt",
                                          file= [("All Files","*.*"),
                                                 ("Text Docs","*.txt")])
    try:
        if file is None:
            return
        window.title(os.path.basename(file))
        text.delete(1.0, END)
        file = open(file,"r")
        text.insert(1.0, file.read())

    except Exception:
        print("Couldnt read it :(")
    finally:
        file.close()
    
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
            file.write(text.get(1.0,END))
    
        except Exception:
            print("not gonna work buddy")
        finally:
            file.close()

def cut():
    text.event_generate("<<Cut>>")
def paste():
    text.event_generate("<<Paste>>")
def copy():
    text.event_generate("<<Copy>>")


def color_text():
    color = colorchooser.askcolor(title="Select a Color")[1]
    print(color[1])
    text.config(fg=color)

def color_bg():
    color = colorchooser.askcolor(title="Select a Color")[1]
    print(color[1])
    text.config(bg=color)

def change_font(*args):
    text.config(font=(font_name.get(),size_box.get()))

def about():
    showinfo("About this progam","This is a progam writen by me :D")


window = Tk()
window.title("Text Editor")
file = None

window_height = 720
window_width = 720
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/ 2) - (window_width / 2))
y = int((screen_height/ 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text = Text(window, font=(font_name.get(),font_size.get()))
scrollbar = Scrollbar(text)
window.grid_rowconfigure(0, weight= 1)
window.grid_columnconfigure(0, weight= 1)
text.grid(sticky=N + E + S + W)
scrollbar.pack(side=RIGHT, fill= Y)
text.config(yscrollcommand=scrollbar.set)

frame = Frame(window)
frame.grid()

color_button_text = Button(frame, text="Color Font", command= color_text)
color_button_text.grid(row=0,column=0)
color_button_bg = Button(frame, text="Color Background", command= color_bg)
color_button_bg.grid(row=0,column=1)

font_box = OptionMenu(frame, font_name, *font.families(),command= change_font)
font_box.grid(row=0,column= 2)

size_box = Spinbox(frame, from_= 1, to= 200, textvariable= font_size, command= change_font)
size_box.grid(row=0,column= 3)



menubar = Menu(window)
window.config(menu=menubar)


fileMenu = Menu(menubar, tearoff=  0)
menubar.add_cascade(label="File",menu= fileMenu)
fileMenu.add_command(label="New file",command= new_file)
fileMenu.add_command(label="Open file",command= open_file)
fileMenu.add_command(label="Save file",command= save_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command= quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu= editMenu)
editMenu.add_command(label="Cut",command= cut)
editMenu.add_command(label="Copy",command= copy) 
editMenu.add_command(label="Paste",command= paste)

helpMenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label="Help",menu= helpMenu)
helpMenu.add_command(label="About",command= about)

window.mainloop()