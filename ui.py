from customtkinter import *
import funcs
from tkinter import *

def create_ui():
    app = CTk()
    app.title('Notepad')
    app.geometry('800x600')
    app.minsize(400, 300)
    app.maxsize(1920, 1080)
    
    menu = Menu(app)
    app.config(menu=menu)

    file_menu = Menu(menu, tearoff=0)
    file_menu.add_command(label='Create', command=funcs.create)
    file_menu.add_command(label='New window', command=funcs.new_window)
    file_menu.add_command(label='Open', command=funcs.open_file)
    file_menu.add_command(label='Save', command=funcs.save)
    file_menu.add_command(label='Save file as..', command=funcs.save_file)
    file_menu.add_command(label='Page options', command=funcs.page_options)
    file_menu.add_command(label='Print', command=funcs.print)
    file_menu.add_command(label='Exit', command=funcs.exit)
    menu.add_cascade(label='File', menu=file_menu)

    app.mainloop()