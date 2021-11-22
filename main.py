import tkinter as tk
from spt.tk_spt import build_layers

window = tk.Tk()

header = tk.Frame(master=window, width=1500, height=20, bg="white")
header.pack()

width = [1500] * 10
height = [2, 10] * 5
bg = ['black', 'white'] * 5

class Staff:

    width_list = width = [1500] * 10
    height_list = height = [2, 10] * 5
    bg = ['black', 'white'] * 5
    
    def __init__(self, screen_width, linewidth):
        self.width = screen_width
        self.linewidth = linewidth
        
    def create_staff(self):
        build_layers(self.width_list, self.height_list, self.bg, window)

    def create_multiple_staffs(self, number_of_staffs, gap_height=50):
        for i in range(number_of_staffs):
            gap = tk.Frame(master=window, width=1500, height=gap_height, bg='white')
            gap.pack()
            self.create_staff()

staff = Staff(1500, 2)
staff.create_multiple_staffs(5)

window.mainloop()