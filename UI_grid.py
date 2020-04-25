from tkinter import *


def make_grid(puzzle):
    """
    Form the grid
    """
    main = Tk()
    for a in range(9):
        for b in range(9):
            temp = Entry(main)
            temp.grid(row=a, column=b, pady=2)
            entry = puzzle[a][b]
            temp.insert(b, str(entry))
    main.mainloop()