import tkinter as tk

class Dialog(tk.Toplevel):

	def __init__(self, parent, rule=None):
		tk.Toplevel.__init__(self, parent)
		self.transient(parent)

		self.parent = parent
		self.result = None

		body = tk.Frame(self)
		self.intial_focus = self.body(body, rule)
		body.pack(padx=5, pady=5)

		self.buttonbox()
		self.grab_set()
		self.protocol("WN_DELETE_WINDOW", self.cancel)
		self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))
		self.wait_window(self)

	def buttonbox(self):
		box = tk.Frame(self)
		tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)
		tk.Button(box, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)
		self.bind("<Return>", self.ok)
		self.bind("<Escape>", self.cancel)
		box.pack()

	def ok(self, event=None):
		self.withdraw()
		self.update_idletasks()
		self.apply()
		self.cancel()

	def cancel(self, event=None):
		self.parent.focus_set()
		self.destroy()
