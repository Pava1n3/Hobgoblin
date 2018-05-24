from tkinter import *
from creaturemanager.creaturemanagerscreen import *

class ToCreatureManagerScreenButton(Button):
	def __init__(self, container, inputHandler):
		Button.__init__(self, container, text="Creature Manager", command=lambda: inputHandler.HandleInput())
		self.bind("<Button-1>", lambda e : inputHandler.HandleInput())
		
class ToCreatureManagerScreenButtonManager():
	def __init__(self, container, controller):
		self.container = container
		self.controller = controller
	
	def MakeAndDisplayButton(self):
		self.inputHandler = ToCreatureManagerScreenButtonInputHandler(self.controller)
		self.button = ToCreatureManagerScreenButton(self.container, self.inputHandler)
		self.button.grid(row=0, column=1, sticky=N+S+E+W)

class ToCreatureManagerScreenButtonInputHandler():
	def __init__(self, controller):
		self.controller = controller
		
	def HandleInput(self):
		self.controller.switch_page(CreatureManagerScreen)