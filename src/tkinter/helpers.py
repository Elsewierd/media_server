import tkinter as tk
from tkinter import filedialog


def get_directory(prompt: str) -> str:
    root = tk.Tk()
    root.withdraw

    directory = filedialog.askdirectory(title=prompt)

    return directory
