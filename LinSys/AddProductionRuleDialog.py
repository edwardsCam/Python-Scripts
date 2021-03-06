import Dialog as d
from tkinter import Label
from tkinter import Entry as Input

class AddProductionRuleDialog(d.Dialog):

	def body(self, master, existingRule=None):
		Label(master, text= "Symbol:"     ).grid(row=0)
		Label(master, text= "Replacement:").grid(row=1)
		self.e1 = Input(master)
		self.e2 = Input(master)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		if existingRule:
			self.e1.insert(0, existingRule[1])
			self.e2.insert(0, existingRule[2])
		return self.e1

	def validate(self):
		symb = self.e1.get()
		rep = self.e2.get()
		if symb and rep:
			return (symb.strip(), rep.strip())

	def apply(self):
		r = self.validate()
		if r:
			self.result = (r[0], r[1])
