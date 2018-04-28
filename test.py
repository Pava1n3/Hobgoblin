#http://thinkingtkinter.sourceforge.net/
from tkinter import *

class HobGoblin:                       
	creatureArray = []
	creatureCount = 0		
  
	def __init__(self, parent):      
		self.mainContainer = Frame(parent) #Create a container, which stores data but displays nothing
		self.mainContainer.pack()
		self.creatureContainer = Frame(parent)
		
		self.makeCreatureButton = Button(self.mainContainer, text="Click me!", background="red") #Button stored in mainContainer, a 'widget'
		self.makeCreatureButton.pack()
		self.makeCreatureButton.bind("<Button-1>", self.makeCreatureButtonClick)  
		
	def makeCreatureButtonClick(self, event):      
		#self.makeCreatureButton.configure(text="Clicked!")
		self.button2 = Button(self.mainContainer, text=str(self.creatureCount) + "The Child" + str(event.x), command= lambda : self.button2.destroy())
		self.button2.bind("<Button-1>", lambda e : self.button2.destroy()) #sketchy af atm
		self.button2.pack(side=LEFT)

root = Tk()
hobGoblin = HobGoblin(root)
root.wm_attributes("-topmost", 1) 
root.mainloop()