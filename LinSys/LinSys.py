from tkinter import Tk
from tkinter import Frame
from tkinter import Menu
from tkinter import Button
from tkinter import Label
from tkinter import Canvas
from tkinter import Scale as Slider
from tkinter import Listbox as List
from tkinter import Entry as Input
from tkinter import Text as Output
from tkinter import StringVar as String
from tkinter import IntVar as Int
from tkinter import END
from tkinter import RIDGE
from tkinter import BROWSE
from tkinter import HORIZONTAL
from tkinter import filedialog
from tkinter.ttk import Combobox as DropDown
import AddProductionRuleDialog as dp
import AddDrawingRuleDialog as dd
import Rule
import Draw
import Generator

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def generate(self):
        n = int(self.menu_gen.get())
        seed = self.inp_seed.get()
        self.output = Generator.convert(seed, n)
        self.generated = True
        self.clearOutput(self.output)

    def draw(self, n, step=False):
        p1, p2 = Draw.move(n)
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=self.color, width=self.thick)
        if step:
            self.canvas.update_idletasks()

    def do(self, action, step):
        if len(action) > 1:
            p = action[1]
        else:
            p = 1.0

        self.timebuff += step
        cmd = action[0].lower()
        if cmd == "draw":
            if self.timebuff > 1.0:
                truncate = int(self.timebuff)
                self.after(truncate, self.draw(float(p), True))
                self.timebuff -= truncate
            else:
                self.draw(float(p))
        elif cmd == "turn":
            Draw.turn(float(p))
        elif cmd == "skip":
            Draw.skip(float(p))
        elif cmd == "back":
            Draw.back(float(p))
        elif cmd == "color":
            self.color = p.replace('_', ' ')
        elif cmd == "thick":
            self.thick = int(p)
        else:
            print("Unknown command " + cmd)

    def drawAll(self):
        self.timebuff = 0.0
        self.color = 'black'
        self.thick = 5
        if self.generated == True:
            l = float(self.slid_linesize.get())
            a = float(self.slid_angle.get())
            Draw.init(self.startingPoint, l, a)
            self.canvas.delete("all")
            step = 1.0/len(self.output)
            percent = 0.0
            for c in self.output:
                if c == '[':
                    Draw.push()
                elif c == ']':
                    Draw.pop()
                else:
                    percent += step
                    color = hex(int(16777215 * percent)).split('x')[1]
                    while len(color) < 6:
                        color = "0" + color
                    self.color = "#" + color
                    #print(self.color)
                    rules = Rule.getDrawings()
                    for r in rules:
                        if c == r[0]:
                            if len(r) > 2:
                                params = (r[1], r[2])
                            else:
                                params = (r[1],)
                            self.do(params, float(self.slid_timer.get()))
                            break


                            

    def clearOutput(self, replacement=None):
        self.text_output.config(state='normal')
        self.text_output.delete(1.0, END)
        if replacement:
            self.text_output.insert(END, replacement)
        self.text_output.config(state='disabled')

    def formatRules(self, rules):
        ret = []
        for r in rules:
            entry = r[0] + " | " + r[1]
            if len(r) > 2:
                entry += " " + r[2]
            ret.append(entry)
        return ret

    def getRuleFromFormatted(self, s):
        if s:
            rule = s.split('|')
            rule[0] = rule[0].strip()
            rule[1] = rule[1].strip()
            prod = rule[1].split(" ")
            if len(prod) == 1:
                return (rule[0], prod[0])
            else:
                return (rule[0], prod[0], prod[1])

    def RefreshLists(self):
        self.list_prod.delete(0, END)
        self.list_draw.delete(0, END)

        l = self.formatRules(Rule.getProductions())
        for p in l:
            self.list_prod.insert(END, p)

        l = self.formatRules(Rule.getDrawings())
        for d in l:
            self.list_draw.insert(END, d)




    def AddProductionRule(self, edit=None):
        rule = dp.AddProductionRuleDialog(self, edit).result
        if rule:
            if edit:
                Rule.removeProd(edit[0])
            Rule.AddProduction(rule)
            self.RefreshLists()

    def AddDrawingRule(self, edit=None):
        rule = dd.AddDrawingRuleDialog(self, edit).result
        if rule:
            if edit:
                Rule.removeDraw(edit[0])
            Rule.AddDrawing(rule)
            self.RefreshLists()

    def EditProductionRule(self):
        s = self.list_prod.curselection()
        if s:
            idx = s[0]
            rule = (idx,) + self.getRuleFromFormatted(self.list_prod.get(idx))
            if rule:
                self.AddProductionRule(rule)

    def EditDrawingRule(self):
        s = self.list_draw.curselection()
        if s:
            idx = s[0]
            rule = (idx,) + self.getRuleFromFormatted(self.list_draw.get(idx))
            if rule:
                self.AddDrawingRule(rule)

    def DeleteProductionRule(self):
        s = self.list_prod.curselection()
        if s:
            Rule.removeProd(s[0])
            self.RefreshLists()

    def DeleteDrawingRule(self):
        s = self.list_draw.curselection()
        if s:
            Rule.removeDraw(s[0])
            self.RefreshLists()




    def packAxiom(self):
        return "@" + str(self.inp_seed.get()).strip()

    def packRules(self, rules):
        ret = "@"
        for r in rules:
            ret += "$" + str(r[0]) + "|" + str(r[1])
            if len(r) > 2:
                ret += ":" + str(r[2])
        return ret

    def packProdRules(self):
        return self.packRules(Rule.getProductions())

    def packDrawRules(self):
        return self.packRules(Rule.getDrawings())


    def parseProdRules(self, raw):
        rules = raw.split('$')
        for rule in rules:
            if rule is not "":
                r = rule.split('|')
                Rule.AddProduction((r[0], r[1]))

    def parseDrawRules(self, raw):
        rules = raw.split('$')
        for rule in rules:
            if rule is not "":
                r = rule.split('|')
                p = r[1].split(':')
                if len(p) == 1:
                    tup = (r[0], p[0])
                else:
                    tup = (r[0], p[0], p[1])
                Rule.AddDrawing(tup)


    def parseSaveFile(self, s):
        Rule.wipe()
        settings = s.split('@')
        self.inp_seed.set(str(settings[1]))
        self.parseProdRules(settings[2])
        self.parseDrawRules(settings[3])
        self.RefreshLists()


    def save(self):
        output = ""
        output += self.packAxiom()
        output += self.packProdRules()
        output += self.packDrawRules()
        try:
            filename = filedialog.asksaveasfilename(**self.file_options)
            if filename:
                f = open(filename, 'w')
                f.write(output)
                f.close()
        except Exception as e:
            print("File IO error in save\n", e)

    def load(self):
        try:
            filename = filedialog.askopenfilename(**self.file_options)
            if filename:
                f = open(filename, 'r')
                self.parseSaveFile(f.read())
                f.close()
                self.slid_linesize.set(1.0)
                self.slid_timer.set(0.0)
                self.menu_gen.set(1)
                self.clearOutput()

        except Exception as e:
            print("File IO error in load\n" + e)




    def click(self, event):
        self.startingPoint = (event.x, event.y)

    def makeMenuBar(self):
        self.menubar = Menu(self);
        self.menubar.add_command(label="Save", command= self.save)
        self.menubar.add_command(label="Load", command= self.load)
        root.config(menu= self.menubar)

    def makeInputFrame(self):
        self.inp_seed         = String()
        self.gen_value        = Int()
        self.fram_input       = Frame(self,              bd= 2, relief= self.style, width= 300, height= 900)
        self.fram_seed        = Frame(self.fram_input,   bd= 1, relief= self.style)
        self.fram_prod        = Frame(self.fram_input,   bd= 1, relief= self.style)
        self.fram_draw        = Frame(self.fram_input,   bd= 1, relief= self.style)
        self.fram_slide       = Frame(self.fram_input,   bd= 1, relief= self.style)
        self.fram_gen         = Frame(self.fram_input,   bd= 1, relief= self.style)
        self.fram_output      = Frame(self.fram_input,   bd= 1, relief= self.style)
        self.menu_gen         = DropDown(self.fram_gen,  textvariable= self.gen_value)
        self.entr_seed        = Input(self.fram_seed,    textvariable= self.inp_seed)
        self.text_output      = Output(self.fram_output, width= 35, height= 10)
        self.list_prod        = List(self.fram_prod,     selectmode= BROWSE, font= "Courier 8", height= 5)
        self.list_draw        = List(self.fram_draw,     selectmode= BROWSE, font= "Courier 8", height= 5)
        self.slid_linesize    = Slider(self.fram_slide,  from_= 0.1, to= 10.0, orient=HORIZONTAL, resolution= 0.1, length= 180)
        self.slid_timer       = Slider(self.fram_slide,  from_= 0, to= 5,          orient= HORIZONTAL, resolution= 0.05, length= 180)
        self.slid_angle       = Slider(self.fram_slide,  from_= 0, to= 359,        orient= HORIZONTAL, length= 180)
        self.butt_prodAdd     = Button(self.fram_prod,   text= "Add",    width=8, command= self.AddProductionRule)
        self.butt_prodEdit    = Button(self.fram_prod,   text= "Edit",   width=8, command= self.EditProductionRule)
        self.butt_prodDelete  = Button(self.fram_prod,   text= "Delete", width=8, command= self.DeleteProductionRule)
        self.butt_drawAdd     = Button(self.fram_draw,   text= "Add",    width=8, command= self.AddDrawingRule)
        self.butt_drawEdit    = Button(self.fram_draw,   text= "Edit",   width=8, command= self.EditDrawingRule)
        self.butt_drawDelete  = Button(self.fram_draw,   text= "Delete", width=8, command= self.DeleteDrawingRule)
        Label(self.fram_seed,   text= "Axiom:", width=8).grid(row=0, column=0)
        Label(self.fram_prod,   text= "Production\nRules:", width=8).grid(row=0, column=0)
        Label(self.fram_draw,   text= "Drawing\nRules:", width=8).grid(row=0, column=0)
        Label(self.fram_slide,  text= "Line Size:").grid(row=0, column=0)
        Label(self.fram_slide,  text= "Delay (ms):").grid(row=1, column=0)
        Label(self.fram_slide,  text= "Starting Angle:").grid(row=2, column=0)
        Label(self.fram_output, text= "Output:").grid(row=0, column=0)
        Label(self.fram_gen,    text= "Generations:").grid(row=0, column=0)

        self.gen_value.set(1)
        self.menu_gen['values'] = tuple(range(1, 13))
        self.slid_linesize.set(1.0)
        self.text_output.config(state='disabled')

        self.fram_input.grid(     row=0, column=0)
        self.fram_seed.grid(      row=1, column=0, sticky='ew')
        self.fram_prod.grid(      row=2, column=0, sticky='ew')
        self.fram_draw.grid(      row=3, column=0, sticky='ew')
        self.fram_slide.grid(     row=4, column=0, sticky='ew')
        self.fram_gen.grid(       row=5, column=0, sticky='ew')
        self.fram_output.grid(    row=6, column=0, sticky='ew')
        self.entr_seed.grid(      row=0, column=1, sticky='ew')
        self.list_prod.grid(      row=0, column=1, sticky='ew')
        self.butt_prodAdd.grid(   row=1, column=0, sticky='ew')
        self.butt_prodEdit.grid(  row=1, column=1, sticky='ew')
        self.butt_prodDelete.grid(row=1, column=2, sticky='ew')
        self.list_draw.grid(      row=0, column=1)
        self.butt_drawAdd.grid(   row=1, column=0, sticky='ew')
        self.butt_drawEdit.grid(  row=1, column=1, sticky='ew')
        self.butt_drawDelete.grid(row=1, column=2, sticky='ew')
        self.slid_linesize.grid(  row=0, column=1, sticky='e')
        self.slid_timer.grid(     row=1, column=1, sticky='e')
        self.slid_angle.grid(     row=2, column=1, sticky='e')
        self.menu_gen.grid(       row=0, column=1)
        self.text_output.grid(    row=1, column=0)

    def makeCanvasFrame(self):
        self.fram_canvas = Frame(self, bd=10, relief=self.style)
        self.canvas      = Canvas(self.fram_canvas, width=900, height=580)
        self.fram_canvas.grid(row=0, column=1, sticky='nesw')
        self.canvas.grid(sticky='nesw')
        self.canvas.bind("<Button-1>", self.click)

    def makeIgnitionFrame(self):
        self.fram_ignition = Frame(self, bd=4, relief=self.style)
        self.butt_generate = Button(self.fram_ignition, text=" -- GENERATE -- ", width=100, command= self.generate)
        self.butt_draw     = Button(self.fram_ignition, text=" -- DRAW -- ", width=100, command= self.drawAll)
        self.fram_ignition.grid(row=1, column=0, columnspan=2)
        self.butt_generate.grid()
        self.butt_draw.grid()

    def createWidgets(self):
        self.style         = RIDGE
        self.startingPoint = (20, 20)
        self.generated     = False
        self.file_options = {}
        self.file_options['defaultextension'] = '.txt'
        self.file_options['filetypes'] = [('Plaintext', '.txt')]
        self.file_options['initialdir'] = 'Patterns'
        self.makeMenuBar()
        self.makeInputFrame()
        self.makeCanvasFrame()
        self.makeIgnitionFrame()

root = Tk()
root.title("Lindenmayer Systems")
root.geometry("1270x680+0+0")
#root.wm_iconbitmap('icon.ico')
app = Application(master=root)
app.mainloop()
