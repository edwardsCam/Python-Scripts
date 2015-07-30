import tkinter as tk
from tkinter import ttk
import AddRuleDialog as d
import Rule
import Draw
import Generator

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def format(self, rules):
        ret = []
        maxlen = 0
        for r in rules:
            l = len(r[0])
            if l > maxlen:
                maxlen = l
        for r in rules:
            entry = ' ' * (maxlen - len(r[0]))
            entry += r[0] + " | " + r[1]
            ret.append(entry)
        return ret

    def getRuleFromFormatted(self, s):
        if s:
            l = s.split('|')
            return (l[0].strip(), l[1].strip())

    def RefreshLists(self):
        self.list_prod.delete(0, tk.END)
        self.list_draw.delete(0, tk.END)
        prod = self.format(Rule.getProductions())
        draw = self.format(Rule.getDrawings())
        for p in prod:
            self.list_prod.insert(tk.END, p)
        for d in draw:
            self.list_draw.insert(tk.END, d)

    def AddProductionRule(self, edit=None):
        rule = d.AddRuleDialog(self, 0, edit).result
        if rule:
            if edit:
                Rule.removeProd(edit[2])
            Rule.AddProduction(rule)
            self.RefreshLists()

    def EditProductionRule(self):
        s = self.list_prod.curselection()
        if s:
            idx = s[0]
            rule = self.getRuleFromFormatted(self.list_prod.get(idx)) + (idx,)
            if rule:
                self.AddProductionRule(rule)

    def DeleteProductionRule(self):
        s = self.list_prod.curselection()
        if s:
            Rule.removeProd(s[0])
            self.RefreshLists()

    def AddDrawingRule(self, edit=None):
        rule = d.AddRuleDialog(self, 1, edit).result
        if rule:
            if edit:
                Rule.removeDraw(edit[2])
            Rule.AddDrawing(rule)
            self.RefreshLists()

    def EditDrawingRule(self):
        s = self.list_draw.curselection()
        if s:
            idx = s[0]
            rule = self.getRuleFromFormatted(self.list_draw.get(idx)) + (idx,)
            if rule:
                self.AddDrawingRule(rule)

    def DeleteDrawingRule(self):
        s = self.list_draw.curselection()
        if s:
            Rule.removeDraw(s[0])
            self.RefreshLists()

    def generate(self):
        n = int(self.menu_gen.get())
        seed = self.inp_seed.get()
        self.output = Generator.convert(seed, n)
        self.generated = True
        self.text_output.config(state='normal')
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, self.output)
        self.text_output.config(state='disabled')

    def draw(self, n, step=False):
        p1, p2 = Draw.move(n)
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1])
        if step:
            self.canvas.update_idletasks()

    def do(self, action):
        params = action.split(' ')
        cmd = params[0].lower()
        if len(params) > 1:
            n = float(params[1])
        else:
            n = 1.0
        if cmd == "draw":
            step = int(self.slid_timer.get())
            if step > 0:
                self.after(step, self.draw(n, True))
            else:
                self.draw(n)
        elif cmd == "turn":
            Draw.turn(n)
        elif cmd == "skip":
            Draw.skip(n)
        elif cmd == "back":
            Draw.back(n)
        else:
            print("Unknown command " + cmd)

    def drawAll(self):
        if self.generated == True:
            l = float(self.slid_linesize.get())
            a = float(self.slid_angle.get())
            Draw.set(self.startingPoint, l, a)
            self.canvas.delete("all")
            for c in self.output:
                for r in Rule.getDrawings():
                    if c == r[0]:
                        self.do(r[1])
                        break

    def click(self, event):
        self.startingPoint = (event.x, event.y)

    def makeInputFrame(self):
        self.inp_seed = tk.StringVar()
        self.gen_value = tk.IntVar()
        self.fram_input = tk.Frame(self, bd=2, relief=self.style, width=300, height=900)
        self.fram_seed = tk.Frame(self.fram_input, bd=1, relief=self.style)
        self.fram_prod = tk.Frame(self.fram_input, bd=1, relief=self.style)
        self.fram_draw = tk.Frame(self.fram_input, bd=1, relief=self.style)
        self.fram_slide = tk.Frame(self.fram_input, bd=1, relief=self.style)
        self.fram_gen = tk.Frame(self.fram_input, bd=1, relief=self.style)
        self.fram_output = tk.Frame(self.fram_input, bd=1, relief=self.style)
        self.menu_gen = ttk.Combobox(self.fram_gen, textvariable= self.gen_value)
        self.entr_seed = tk.Entry(self.fram_seed, textvariable= self.inp_seed)
        self.text_output = tk.Text(self.fram_output, width=35, height=10)
        self.list_prod = tk.Listbox(self.fram_prod, selectmode= tk.BROWSE, font="Courier 8")
        self.list_draw = tk.Listbox(self.fram_draw, selectmode= tk.BROWSE, font="Courier 8")
        self.slid_linesize = tk.Scale(self.fram_slide, from_=0.1, to=10.0, orient=tk.HORIZONTAL, resolution=0.1, length=180)
        self.slid_timer = tk.Scale(self.fram_slide, from_=0, to=100, orient=tk.HORIZONTAL, length=180)
        self.slid_angle = tk.Scale(self.fram_slide, from_=0, to=359, orient=tk.HORIZONTAL, length=180)
        self.butt_prodAdd = tk.Button(self.fram_prod, text="Add", width=8, command= self.AddProductionRule)
        self.butt_prodEdit = tk.Button(self.fram_prod, text="Edit", width=8, command= self.EditProductionRule)
        self.butt_prodDelete = tk.Button(self.fram_prod, text="Delete", width=8, command= self.DeleteProductionRule)
        self.butt_drawAdd = tk.Button(self.fram_draw, text="Add", width=8, command= self.AddDrawingRule)
        self.butt_drawEdit = tk.Button(self.fram_draw, text="Edit", width=8, command= self.EditDrawingRule)
        self.butt_drawDelete = tk.Button(self.fram_draw, text="Delete", width=8, command= self.DeleteDrawingRule)
        tk.Label(self.fram_seed, text="Seed:", width=8).grid(row=0, column=0)
        tk.Label(self.fram_prod, text="Production\nRules:", width=8).grid(row=0, column=0)
        tk.Label(self.fram_draw, text="Drawing\nRules:", width=8).grid(row=0, column=0)
        tk.Label(self.fram_slide, text="Line Size:").grid(row=0, column=0)
        tk.Label(self.fram_slide, text="Delay (ms):").grid(row=1, column=0)
        tk.Label(self.fram_slide, text="Starting Angle:").grid(row=2, column=0)
        tk.Label(self.fram_output, text="Output:").grid(row=0, column=0)
        self.labl_gen = tk.Label(self.fram_gen, text="Generations:").grid(row=0, column=0)

        self.gen_value.set(1)
        self.menu_gen['values'] = tuple(range(1, 13))
        self.slid_linesize.set(1.0)
        self.text_output.config(state='disabled')

        self.fram_input.grid(row=0, column=0)
        self.fram_seed.grid(row=1, column=0, sticky='ew')
        self.fram_prod.grid(row=2, column=0, sticky='ew')
        self.fram_draw.grid(row=3, column=0, sticky='ew')
        self.fram_slide.grid(row=4, column=0, sticky='ew')
        self.fram_gen.grid(row=5, column=0, sticky='ew')
        self.fram_output.grid(row=6, column=0, sticky='ew')
        self.entr_seed.grid(row=0, column=1, sticky='ew')
        self.list_prod.grid(row=0, column=1, stick='ew')
        self.butt_prodAdd.grid(row=1, column=0, sticky='ew')
        self.butt_prodEdit.grid(row=1, column=1, sticky='ew')
        self.butt_prodDelete.grid(row=1, column=2, sticky='ew')
        self.list_draw.grid(row=0, column=1)
        self.butt_drawAdd.grid(row=1, column=0, sticky='ew')
        self.butt_drawEdit.grid(row=1, column=1, sticky='ew')
        self.butt_drawDelete.grid(row=1, column=2, sticky='ew')
        self.slid_linesize.grid(row=0, column=1, sticky='e')
        self.slid_timer.grid(row=1, column=1, sticky='e')
        self.slid_angle.grid(row=2, column=1, sticky='e')
        self.menu_gen.grid(row=0, column=1)
        self.text_output.grid(row=1, column=0)

    def makeCanvasFrame(self):
        self.fram_canvas = tk.Frame(self, bd=10, relief=self.style)
        self.canvas = tk.Canvas(self.fram_canvas, width=1400, height=800)
        self.fram_canvas.grid(row=0, column=1, sticky='nesw')
        self.canvas.grid(sticky='nesw')
        self.canvas.bind("<Button-1>", self.click)

    def makeIgnitionFrame(self):
        self.fram_ignition = tk.Frame(self, bd=4, relief=self.style)
        self.butt_generate = tk.Button(self.fram_ignition, text=" -- GENERATE -- ", width=100, command= self.generate)
        self.butt_draw = tk.Button(self.fram_ignition, text=" -- DRAW -- ", width=100, command= self.drawAll)
        self.fram_ignition.grid(row=1, column=0, columnspan=2)
        self.butt_generate.grid()
        self.butt_draw.grid()

    def createWidgets(self):
        self.startingPoint = (20, 20)
        Draw.set(self.startingPoint)
        self.style = tk.RIDGE
        self.makeInputFrame()
        self.makeCanvasFrame()
        self.makeIgnitionFrame()

root = tk.Tk()
root.title("Lindenmayer Systems")
root.geometry("1800x900+30+30")
#root.wm_iconbitmap('icon.ico')
app = Application(master=root)
app.mainloop()
