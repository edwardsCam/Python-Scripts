import Dialog as d
import tkinter as tk

class AddRuleDialog(d.Dialog):

	def body(self, master, t, rule=None):
		tk.Label(master, text="Symbol:").grid(row=0)
		if t == 0:
			tk.Label(master, text="Replacement:").grid(row=1)
		else:
			tk.Label(master, text="Drawing Rule:").grid(row=1)
		self.e1 = tk.Entry(master)
		self.e2 = tk.Entry(master)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		if rule:
			self.e1.insert(0, rule[0])
			self.e2.insert(0, rule[1])
		return self.e1

	def apply(self):
		symb = self.e1.get().strip()
		repl = self.e2.get().strip()
		if symb and repl:
			self.result = (symb, repl)
