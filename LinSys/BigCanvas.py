import tkinter as tk

class BigCanvas(tk.Toplevel):

    def __init__(self, parent, **kwargs):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent

        padx = 50
        pady = 100
        w = parent.winfo_screenwidth()-padx
        h = parent.winfo_screenheight()-pady
        dimensions = "{0}x{1}+0+0".format(w, h)

        self.canvas = tk.Canvas(self, width= w, height= h)
        self.canvas.bind("<Button-1>", parent.clickAndRedraw)
        self.canvas.pack()
        self.geometry(dimensions)

    def canvas(self):
        return self.canvas
