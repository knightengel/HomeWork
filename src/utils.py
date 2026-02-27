import tkinter as tk
from tkinter import filedialog, simpledialog

def choose_directory(title="Выберите папку для поиска"):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    return folder_path

def choose_save_file(title="Куда сохранить лог?", default_ext=".log", initial_file="keyword_search.log"):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title=title,
        initialfile=initial_file,
        defaultextension=default_ext,
        filetypes=[("Log files", "*.log"), ("All files", "*.*")]
    )
    return file_path

def ask_keyword():
    root = tk.Tk()
    root.withdraw()
    keyword = simpledialog.askstring("Ввод данных", "Введите ключевое слово (или regex) для поиска:")
    return keyword
