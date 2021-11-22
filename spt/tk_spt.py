import tkinter as tk


def build_layers(width: list, height: list, bg: list, master) -> None:
    if len(width) != len(height) != len(bg):
        raise ValueError('Lists must be the same size!')
    
    for w, h, c in zip(width, height, bg):
        frame = tk.Frame(master=master, width=w, height=h, bg=c)
        frame.pack()
    
    return