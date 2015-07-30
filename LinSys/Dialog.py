import tkinter as tk
import os

class Dialog(tk.Toplevel):

	def __init__(self, parent, t, rule=None):
		tk.Toplevel.__init__(self, parent)
		self.transient(parent)

		if t == 0:
			self.title("Add Production Rule")
		else:
			self.title("Add Drawing Rule")

		self.parent = parent
		self.result = None

		body = tk.Frame(self)
		self.intial_focus = self.body(body, t, rule)
		body.pack(padx=5, pady=5)

		self.buttonbox()
		self.grab_set()

		#if not self.initial_focus:
		#	self.initial_focus = self

		self.protocol("WN_DELETE_WINDOW", self.cancel)

		self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))

		#self.initial_focus.focus_set()
		self.wait_window(self)

	def body(self, master):
		pass

	def buttonbox(self):
		box = tk.Frame(self)
		w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
		w.pack(side=tk.LEFT, padx=5, pady=5)
		w = tk.Button(box, text="Cancel", width=10, command=self.cancel)
		w.pack(side=tk.LEFT, padx=5, pady=5)

		self.bind("<Return>", self.ok)
		self.bind("<Escape>", self.cancel)

		box.pack()

	def ok(self, event=None):
		if not self.validate():
			self.initial_focus.focus_set()
			return

		self.withdraw()
		self.update_idletasks()

		self.apply()
		self.cancel()

	def cancel(self, event=None):
		self.parent.focus_set()
		self.destroy()

	def validate(self):
		return 1 #override

	def apply(self):
		pass
