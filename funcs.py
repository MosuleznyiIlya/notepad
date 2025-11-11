import ui
import libs
import main as __main__
from tkinter import filedialog, messagebox
from customtkinter import *

def save_file():
    file_name = filedialog.asksaveasfile(initialdir='/', title='Select file')
    if file_name:
        f = open(file_name, 'w')
        text_save = str(ui.text.get(1.0, 'end'))
        f.write(text_save + '\n')
        f.close()
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[('Text files', '*.txt'), ('All files', '*.*')],
        title='Open file'
    )
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_content = f.read()
        ui.text.delete(1.0, 'end')
        ui.text.insert('end', text_content)
def create():
    ui.text.delete('1.0', 'end')
def exit():
    ui.app.destroy()
def new_window():
    main_file = libs.os.path.join(libs.os.path.dirname(__file__), 'main.py')
    libs.subprocess.Popen([libs.sys.executable, main_file])
def save():
    pass
def page_options():
    pass
def print():
    pass
def undo():
    pass
def cut():
    try:
        ui.text.event_generate('<<Cut>>')
    except Exception as e:
        print(f'Cut failed: {e}')
def copy():
    try:
        ui.text.event_generate('<<Copy>>')
    except Exception as e:
        print(f'Copy failed: {e}')
def insert():
    try:
        ui.text.event_generate('<<Paste>>')
    except Exception as e:
        print(f'Paste failed: {e}')
def delete():
    try:
        ui.text.event_generate('<<Clear>>')
    except Exception as e:
        print(f'Delete failed: {e}')
def find():
    pass
def select_all():
    ui.text.tag_add('sel', '1.0', 'end')
def find_next():
    pass
def find_earlier():
    pass
def replace():
    pass
def go():
    pass
def time_and_date():
    pass
def wrapping():
    pass
def font():
    pass
def scale():
    scale_value_input = CTkInputDialog(title='Scale', text='Enter font size (e.g., 12):')
    scale_value = scale_value_input.get_input()
    if scale_value and scale_value.isdigit():
        ui.text.configure(font=('Arial', int(scale_value)))
def row_state():
    cursor_position = ui.text.index('insert')
    row, col = cursor_position.split('.')
    messagebox.showinfo('Row State', f'Row: {row}, Column: {col}')
def help():
    help_box = CTkToplevel()
    help_box.title('Help')
    help_box.geometry('300x200')
    help_box.resizable(False, False)

    help_box.after(100, lambda: help_box.lift())
    help_box.attributes('-topmost', True)
    help_box.after_idle(help_box.attributes, '-topmost', False)

    help_label = CTkLabel(help_box, text='Binds:\nCopy - Ctrl+C\nPaste - Ctrl+VCut - Ctrl+X\nUndo - Ctrl+Z\nSave - Ctrl+S\n Delete - Delete\nFind - Ctrl+F\nSelleact all - Ctrl+A\n Help - F1')
    help_label.pack(pady=10)

def send_feedback():
    pass
def about():
    pass
