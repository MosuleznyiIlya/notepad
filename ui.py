from customtkinter import *
from tkinter import *
import funcs

text = None

def toggle_theme():
    current = get_appearance_mode()
    if current == "Dark":
        set_appearance_mode("Light")
    else:
        set_appearance_mode("Dark")

def create_ui():
    global text

    app = CTk()
    app.title('Notepad')
    app.geometry('800x600')
    app.minsize(400, 300)
    
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

    edit_menu = Menu(menu, tearoff=0)
    edit_menu.add_command(label='Undo', command=funcs.undo)
    edit_menu.add_command(label='Cut', command=funcs.cut)
    edit_menu.add_command(label='Copy', command=funcs.copy)
    edit_menu.add_command(label='Insert', command=funcs.insert)
    edit_menu.add_command(label='Delete', command=funcs.delete)
    edit_menu.add_command(label='Find', command=funcs.find)
    edit_menu.add_command(label='Find next', command=funcs.find_next)
    edit_menu.add_command(label='Find earlier', command=funcs.find_earlier)
    edit_menu.add_command(label='Replace', command=funcs.replace)
    edit_menu.add_command(label='Go', command=funcs.go)
    edit_menu.add_command(label='Select all', command=funcs.select_all)
    edit_menu.add_command(label='Time and date', command=funcs.time_and_date)
    menu.add_cascade(label='Edit', menu=edit_menu)

    format_menu = Menu(menu, tearoff=0)
    format_menu.add_command(label='Word wrapping', command=funcs.wrapping)
    format_menu.add_command(label='Font', command=funcs.Font)
    menu.add_cascade(label='Format', menu=format_menu)

    view_menu = Menu(menu, tearoff=0)
    view_menu.add_command(label='Scale', command=funcs.scale)
    view_menu.add_command(label='Row state', command=funcs.row_state)
    view_menu.add_command(label=f'Click to change themes(now - {get_appearance_mode()})', command=toggle_theme)
    menu.add_cascade(label='View', menu=view_menu)

    help_menu = Menu(menu, tearoff=0)
    help_menu.add_command(label='Help', command=help)
    help_menu.add_command(label='Send feedback', command=funcs.send_feedback)
    help_menu.add_command(label='About', command=funcs.about)
    menu.add_cascade(label='Help', menu=help_menu)

    text=CTkTextbox(app, fg_color='transparent')
    text.pack(expand=YES, fill=BOTH)

    app.mainloop()