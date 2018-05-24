from tkinter import *
from geometrymanager.addtogrid import AddToGrid as hGrid

class CreatureManagerScreen(Frame):
	def __init__(self, container, controller):
		Frame.__init__(self, container) #init takes a master, which is container which is HobGoblin.mainContainer
		
		root = controller.getRoot()
		self.creatureManagerMenuBar = Menu(root)
		self.creatureManagerMenuBar.add_command(label="New")
		self.creatureManagerMenuBar.add_command(label="Open")
		self.creatureManagerMenuBar.add_separator()
		self.creatureManagerMenuBar.add_command(label="Main Menu")
	
		self.setupButtons()
		self.setupBigBlock()
		#self.grid_columnconfigure(0, weight=0)
		#self.grid_rowconfigure(0, weight=0)
		
	def setupButtons(self):
		self.newButton = Button(self, text="New", background="grey")#, width=5, height=5)
		self.openButton = Button(self, text="Open", background="grey")#, width=5, height=5)
		self.saveButton = Button(self, text="Save", background="grey")#, width=5, height=5)
		self.toMenuButton = Button(self, text="Menu", background="grey")#, width=5, height=5)
		
		#hGrid.grid(self.newButton)
		#hGrid.grid(self.openButton, 0, 1)
		#hGrid.grid(self.saveButton, 0, 2)
		#hGrid.grid(self.toMenuButton, 0, 3, "nse")
		
	def setupBigBlock(self):
		self.bigBlock = Frame(self, bg="lime", width=250, height=80)
		hGrid.grid(self.bigBlock, 1, 0, "nsew", 4)
		
	def handlePageSwitch(self, root):
		root.config(menu=self.creatureManagerMenuBar)

