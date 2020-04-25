from tkinter import *

def make_grid():
    """
    Form the grid
    """
    main = Tk()
    for a in range(9):
        for b in range(9):
            temp = Entry(main)
            temp.grid(row=a, column=b, pady=2)
    main.mainloop()