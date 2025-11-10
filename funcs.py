import ui
import libs
import main as __main__
from tkinter import filedialog, simpledialog, messagebox

def save_file():
    file_name = filedialog.asksaveasfile(initialdir='/', title='Select file')
    if file_name:
        f = open(file_name, 'w')
        text_save = str(ui.text.get(1.0, 'end'))
        f.write(text_save + "\n")
        f.close()
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Open file"
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
        ui.text.delete(1.0, "end")
        ui.text.insert("end", text_content)
def create():
    ui.text.delete("1.0", 'end')
def exit():
    ui.app.destroy()
def new_window():
    main_file = libs.os.path.join(libs.os.path.dirname(__file__), "main.py")
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
        ui.text.event_generate("<<Cut>>")
    except Exception as e:
        print(f"Cut failed: {e}")
def copy():
    try:
        ui.text.event_generate("<<Copy>>")
    except Exception as e:
        print(f"Copy failed: {e}")
def insert():
    try:
        ui.text.event_generate("<<Paste>>")
    except Exception as e:
        print(f"Paste failed: {e}")
def delete():
    try:
        ui.text.event_generate("<<Clear>>")
    except Exception as e:
        print(f"Delete failed: {e}")
def find():
    pass
def select_all():
    ui.text.tag_add("sel", "1.0", 'end')
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
def Font():
    pass
def scale():
    scale_value = simpledialog.askstring("Scale", "Enter font size (e.g., 12):")
    if scale_value and scale_value.isdigit():
        ui.text.config(font=("Arial", int(scale_value)))
def row_state():
    cursor_position = ui.text.index("insert")
    row, col = cursor_position.split(".")
    messagebox.showinfo("Row State", f"Row: {row}, Column: {col}")
def help():
    pass
def send_feedback():
    pass
def about():
    pass