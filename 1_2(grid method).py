# Arguments of the grid() geometry manager
'''
column        The column number where you want the widget gridded, counting from zero. The default value is zero.
columnspan    Normally a widget occupies only one cell in the grid. However, you can grab multiple cells of a row and
              merge them into one large cell by setting the columnspan option to the numbers of cells. For example,
              w.grid(row=0, column=2, columnspan=3) would place widget w in a cell that spans columns 2, 3, and 4 of row
              0.
in_           To register w as a child of some widget w2, use in_w2. The new parent w2 must be a descendant of the parent
              widget used when w was created.
ipadx         Internal x padding. This dimension is added inside the widget inside its left and right sides.
ipady         Internal y padding. This dimension is added inside the widget inside its top and bottom borders.
padx          External x padding. This dimension is added to the left and right outside the widget.
pady          External y padding. This dimension is added above and below the widget.
row           The row number into which you want to insert the widget, counting from 0. The default is the next higher
              -numbered unoccupied row.
rowspan       Normally a widget occupies only one cell in the grid. You can grab multiple adjacent cells of a column,
              however, by setting the rowspan option to the number of cells to grab. This option can be used in
              combination with the columnspan option to grab a block of cells. For example, w.grid(row=3, column=2,
              rowspan=4, columnspan=5) would place widget w in an area formed by merging 20 cells, with row numbers 3-6
              and column numbers 2-6
sticky        This option determines how to distibutes any extra within the cell that is not taken up by the widget at
              its natural size.

-You can position the widget in a corner of the cell by using tk.N, tk.E, tk.S, tk.W
Other grid management methods : https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/grid-methods.html

'''
import tkinter as tk

root = tk.Tk()
Button1 = tk.Button(root, text="Button1")
Button1.grid(row=0, column=0, columnspan=3, sticky=tk.EW)
Button2 = tk.Button(root, text="Button2")
Button2.grid(row=1, column=0, rowspan=3, sticky=tk.NS)
for i in range(1, 3):
    for j in range(1, 3):
        button = tk.Button(root, text="Button {} {}".format(i, j))
        button.grid(row=i, column=j, ipadx=i*10, ipady=j*10)
root.mainloop()
