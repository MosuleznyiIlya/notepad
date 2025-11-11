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
    help_box.geometry('400x300')
    help_box.resizable(False, False)

    help_box.after(100, lambda: help_box.lift())
    help_box.attributes('-topmost', True)
    help_box.after_idle(help_box.attributes, '-topmost', False)

    tabview = CTkTabview(help_box)
    tabview.pack(expand=True, fill='both', padx=10, pady=10)

    tabview.add('Binds')

    binds_text = (
        'Binds:\n'
        'Copy - Ctrl+C\n'
        'Paste - Ctrl+V\n'
        'Cut - Ctrl+X\n'
        'Undo - Ctrl+Z\n'
        'Save - Ctrl+S\n'
        'Delete - Delete\n'
        'Find - Ctrl+F\n'
        'Select all - Ctrl+A\n'
        'Help - F1'
    )
    binds_label = CTkLabel(tabview.tab('Binds'), text=binds_text, justify='left')
    binds_label.pack(pady=10, padx=10, anchor='w')
def send_feedback():
    send_box = CTkToplevel()
    send_box.title('Send feedback')
    send_box.geometry('400x300')
    send_box.resizable(False, False)

    send_box.after(100, lambda: send_box.lift())
    send_box.attributes('-topmost', True)
    send_box.after_idle(send_box.attributes, '-topmost', False)

    tabview = CTkTabview(send_box)
    tabview.pack(expand=True, fill='both', padx=10, pady=10)

    tabview.add('Feedback')
    feedback_label = CTkLabel(tabview.tab('Feedback'), text='Send feedback here:')
    feedback_label.pack(pady=10)
    feedback_entry = CTkTextbox(tabview.tab('Feedback'), height=120)
    feedback_entry.pack(padx=10, pady=5, fill='x')
    feedback_button = CTkButton(tabview.tab('Feedback'), text='Send', command=lambda: feedback_entry.delete('1.0', 'end'))
    feedback_button.pack(pady=5)
def about():
    about_box = CTkToplevel()
    about_box.title('Help')
    about_box.geometry('400x300')
    about_box.resizable(False, False)

    about_box.after(100, lambda: about_box.lift())
    about_box.attributes('-topmost', True)
    about_box.after_idle(about_box.attributes, '-topmost', False)

    tabview = CTkTabview(about_box)
    tabview.pack(expand=True, fill='both', padx=10, pady=10)

    tabview.add('Info')

    info_label = CTkLabel(tabview.tab('Info'), text='Custom Notepad\nCreated by Mosuleznyi Ilya', justify='center')
    info_label.pack(pady=2, )