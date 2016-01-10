import Dialog as d
from tkinter import Label

class HelpDialog(d.Dialog):

	def body(self, master, dummy=None):
		helpTxt = "A Lindenmayer System is a text-based formal grammar that can be used to draw patterns governed by a set of well-defined rules."
		Label(master, text=helpTxt).grid(row=0)
		Label(master, text="").grid(row=1)

		helpTxt = "It consists of three components:"
		Label(master, text=helpTxt).grid(row=2)

		helpTxt = "    1. An Axiom"
		Label(master, text=helpTxt).grid(row=3)

		helpTxt = "    2. A set of Production Rules (aka replacements)"
		Label(master, text=helpTxt).grid(row=4)

		helpTxt = "    3. A set of Drawing Rules"
		Label(master, text=helpTxt).grid(row=5)
		Label(master, text="").grid(row=6)

		helpTxt = "The axiom can be any string of text. L-systems often start with an axiom of a single character."
		Label(master, text=helpTxt).grid(row=7)

		helpTxt = "Production Rules control the growth of the system. If there are n generations, the Production Rules are recursively applied n times."
		Label(master, text=helpTxt).grid(row=8)

		helpTxt = "Once generation is completed, the Drawing Rules dictate how to visually represent the resulting string."
		Label(master, text=helpTxt).grid(row=9)
		Label(master, text="").grid(row=10)

		helpTxt = "Here's how it works:"
		Label(master, text=helpTxt).grid(row=11)

		helpTxt = "Starting with the axiom, it will apply all the production rules (replacements) and return the result. If there are multiple generations, it will feed this result into the next generation and repeat the process."
		Label(master, text=helpTxt).grid(row=12)

		helpTxt = "Beware, due to the recursive and exponential nature of L-Systems, these outputs can grow really, REALLY large if you're not careful. If your machine doesn't have much RAM or is otherwise weak-sauce, the program might freeze."
		Label(master, text=helpTxt).grid(row=13)

		helpTxt = "I'd start out with 1 or 2 generations and go up from there ;)"
		Label(master, text=helpTxt).grid(row=14)

		helpTxt = "This results in one long string of characters. Then, letter by letter, it will read through this output and apply the appropriate drawing commands."
		Label(master, text=helpTxt).grid(row=15)

		helpTxt = "If the phrase 'Turtle Graphics' means anything to you, that's what's going on here."
		Label(master, text=helpTxt).grid(row=16)
		Label(master, text="").grid(row=17)

		helpTxt = "So, here's the workflow:"
		Label(master, text=helpTxt).grid(row=18)

		helpTxt = "1. Give it an axiom"
		Label(master, text=helpTxt).grid(row=19)

		helpTxt = "2. Give it some production rules"
		Label(master, text=helpTxt).grid(row=20)

		helpTxt = "3. Give it some drawing rules"
		Label(master, text=helpTxt).grid(row=21)

		helpTxt = "4. Select a number of generations to grow"
		Label(master, text=helpTxt).grid(row=22)

		helpTxt = "5. Hit GENERATE"
		Label(master, text=helpTxt).grid(row=23)

		helpTxt = "6. (optional) Change the line size and/or starting angle"
		Label(master, text=helpTxt).grid(row=24)

		helpTxt = "7. (optional) Set the drawing delay. This will make the program wait x milliseconds before drawing each line. This can let you see the growth of the pattern."
		Label(master, text=helpTxt).grid(row=25)

		helpTxt = "8. Click somewhere on the canvas to designate the starting point"
		Label(master, text=helpTxt).grid(row=26)

		helpTxt = "9. Hit DRAW"
		Label(master, text=helpTxt).grid(row=27)

		helpTxt = "10. ???"
		Label(master, text=helpTxt).grid(row=28)

		helpTxt = "11. Profit"
		Label(master, text=helpTxt).grid(row=29)
		Label(master, text="").grid(row=30)

		helpTxt = "You can load in some existing samples to get started. You can also save patterns for later."
		Label(master, text=helpTxt).grid(row=31)
		Label(master, text="").grid(row=32)
		Label(master, text="").grid(row=33)

		helpTxt = "Developed by Cameron Edwards in 2015/2016"
		Label(master, text=helpTxt).grid(row=34)


	def apply(self):
		pass