from tkinter import *

class CreatureManagerScreen(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent) #init takes a master, which is parent which is HobGoblin
		
		label = Label(self, text="Creature Page")
		