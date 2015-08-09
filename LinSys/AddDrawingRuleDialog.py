import Dialog as d
import tkinter as tk
from tkinter import ttk

class AddDrawingRuleDialog(d.Dialog):

	def body(self, master, existingRule=None):
		self.cmd = tk.StringVar()
		tk.Label(master, text="Symbol:").grid(row=0)
		tk.Label(master, text="Rule:").grid(row=1)
		self.e1 = tk.Entry(master, width=20)
		self.e2 = ttk.Combobox(master, textvariable=self.cmd, width=7)
		self.e3 = tk.Entry(master, width=10)
		self.e2['values'] = ['draw', 'turn', 'skip', 'back', 'color', 'thick']
		self.e1.grid(row=0, column=1, columnspan=2)
		self.e2.grid(row=1, column=1)
		self.e3.grid(row=1, column=2)
		if existingRule:
			r = existingRule[1]
			self.e1.insert(0, existingRule[0])
			self.e2.insert(0, r[0])
			if len(r) > 1:
				self.e3.insert(0, r[1])
		return self.e1

	def validate(self):
		symb = self.e1.get()
		rule = self.e2.get()
		param = self.e3.get()
		if symb and rule:
			symb = symb.strip()
			rule = rule.strip()
			if param:
				rule += " " + str(param)
			return (symb, rule)

	def apply(self):
		r = self.validate()
		if r:
			self.result = (r[0], r[1])
