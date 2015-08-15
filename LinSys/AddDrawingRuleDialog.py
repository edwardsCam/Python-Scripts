import Dialog as d
from tkinter import Label
from tkinter import Entry as Input
from tkinter import StringVar as String
from tkinter.ttk import Combobox as Dropdown

class AddDrawingRuleDialog(d.Dialog):

	def body(self, master, existingRule=None):
		self.cmd = String()
		Label(master, text= "Symbol:").grid(row=0)
		Label(master, text= "Rule:"  ).grid(row=1)
		self.e1 = Input(master, width=20)
		self.e2 = Dropdown(master, textvariable= self.cmd, width= 7, state= 'readonly')
		self.e3 = Input(master, width=10)
		self.e2['values'] = ['draw', 'turn', 'skip', 'back', 'color', 'thick']
		self.e1.grid(row=0, column=1, columnspan=2)
		self.e2.grid(row=1, column=1)
		self.e3.grid(row=1, column=2)
		if existingRule:
			self.e1.insert(0, existingRule[1])
			self.e2.insert(0, existingRule[2])
			if len(existingRule) > 3:
				self.e3.insert(0, existingRule[3])
		return self.e1

	def validate(self):
		symb = self.e1.get()
		rule = self.e2.get()
		param = self.e3.get()
		if symb and rule:
			symb = symb.strip()
			rule = rule.strip()
			if param:
				return (symb, rule, param)
			else:
				return (symb, rule)

	def apply(self):
		r = self.validate()
		if r:
			self.result = r
