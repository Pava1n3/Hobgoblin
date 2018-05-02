#http://thinkingtkinter.sourceforge.net/
from Tkinter import *

creatureCount = 0
creatureArray = []

class HobGoblin:					     
	def __init__(self, parent):		 
		self.mainContainer = Frame(parent) #Create a container, which stores data but displays nothing
		self.mainContainer.pack()
		self.creatureContainer = Frame(parent)
		
		self.makeCreatureButton = Button(self.mainContainer, text="Click me!", background="red") #Button stored in mainContainer, a 'widget'
		self.makeCreatureButton.pack()
		self.makeCreatureButton.bind("<Button-1>", self.makeCreatureButtonClick)  		
		
	def makeCreatureButtonClick(self, event):	
		global creatureArray
		global creatureCount
	
		creature = Button(self.mainContainer, text="Child " + str(creatureCount), command= lambda : creature.destroy())
		creature.id = creatureCount
		creatureArray.append(creature)
		
		creature.bind("<Button-1>", lambda e : creature.destroy()) #sketchy af atm
		creature.pack(side=LEFT)
		creatureCount += 1
				
		

root = Tk()
hobGoblin = HobGoblin(root)
root.wm_attributes("-topmost", 1) 
root.mainloop()