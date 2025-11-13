import ui
import libs
import main as __main__
from tkinter import filedialog, messagebox
from customtkinter import *
from customtkinter import CTkToplevel, CTkLabel, CTkEntry, CTkButton
import os

file_path = None
search_text = ''
last_index = '1.0'
prev_index = 'end'
font_size = 12

def save_file():
    global file_path
    fp = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if fp:
        file_path = fp
        save()
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
    global file_path
    if not file_path:
        save_file()
        return
    text_save = ui.text.get(1.0, 'end')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text_save)
def print():
    text_to_print = ui.text.get(1.0, 'end')
    temp_file = os.path.join(os.environ['TEMP'], 'temp_print.txt')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(text_to_print)
    os.startfile(temp_file, 'print')
def undo():
    try:
        ui.text.edit_undo()
    except Exception:
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
def select_all():
    ui.text.tag_add('sel', '1.0', 'end')
def find():
    global search_text, found_positions, current_index
    find_window = CTkToplevel()
    find_window.title('Найти')
    find_window.geometry('300x120')

    CTkLabel(find_window, text='Введите текст для поиска:').pack(pady=(10,0))
    entry_find = CTkEntry(find_window)
    entry_find.pack(pady=(0,10))

    def do_find():
        global search_text, found_positions, current_index
        search_text = entry_find.get()
        found_positions = []
        current_index = -1

        ui.text.tag_remove('found', '1.0', 'end')
        ui.text.tag_remove('current', '1.0', 'end')

        if search_text:
            start = '1.0'
            while True:
                pos = ui.text.search(search_text, start, stopindex='end')
                if not pos:
                    break
                end_pos = f'{pos}+{len(search_text)}c'
                ui.text.tag_add('found', pos, end_pos)
                found_positions.append((pos, end_pos))
                start = end_pos
            ui.text.tag_config('found', background='yellow')

        find_window.destroy()

    entry_find.bind('<Return>', lambda event: do_find())
def highlight_current():
    ui.text.tag_remove('current', '1.0', 'end')
    if not found_positions or current_index == -1:
        return
    start, end = found_positions[current_index]
    ui.text.tag_add('current', start, end)
    ui.text.tag_config('current', background='orange')
    ui.text.mark_set('insert', end)
    ui.text.see(start)
def find_next():
    global current_index
    if not found_positions:
        return
    current_index += 1
    if current_index >= len(found_positions):
        current_index = 0
    highlight_current()
def find_earlier():
    global current_index
    if not found_positions:
        return
    current_index -= 1
    if current_index < 0:
        current_index = len(found_positions) - 1
    highlight_current()
def replace():
    pass
def go():
    pass
def time_and_date():
    pass
def wrapping():
    pass
def font():
    global font_size

    font_window = CTkToplevel()
    font_window.title('Сменить шрифт')
    font_window.geometry('300x180')

    font_window.attributes('-topmost', True)
    font_window.after(100, lambda: font_window.attributes('-topmost', False))

    label_name = CTkLabel(font_window, text='Имя шрифта:')
    label_name.pack(pady=(10, 0))

    entry_name = CTkEntry(font_window, placeholder_text='Например: Arial')
    entry_name.pack(pady=(0, 10))

    label_size = CTkLabel(font_window, text='Размер шрифта:')
    label_size.pack()

    entry_size = CTkEntry(font_window, placeholder_text=str(font_size))
    entry_size.pack(pady=(0, 10))

    def apply_font():
        global font_size
        font_name = entry_name.get() or 'Arial'
        size_text = entry_size.get()
        font_size = int(size_text) if size_text.isdigit() else font_size
        ui.text.configure(font=(font_name, font_size))
        font_window.destroy()

    apply_btn = CTkButton(font_window, text='Применить', command=apply_font)
    apply_btn.pack(pady=10)
def scale():
    global font_size
    scale_value_input = CTkInputDialog(title='Размер шрифта', text='Введите размер шрифта:')
    scale_value = scale_value_input.get_input()
    if scale_value and scale_value.isdigit():
        font_size = int(scale_value)
        current_font = ui.text.cget('font').split()[0]
        ui.text.configure(font=(current_font, font_size))
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
        'Find next - F3\n'
        'Find earlier - Shift+F3\n'
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
