#http://thinkingtkinter.sourceforge.net/
from Tkinter import *
from PIL import ImageTk, Image

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
	
		"""creature = Button(self.mainContainer, text="Child " + str(creatureCount), command= lambda : creature.destroy())
		creature.id = creatureCount
		creatureArray.append(creature)
		
		creature.bind("<Button-1>", lambda e : creature.destroy())
		creature.pack(side=LEFT)
		print creature.id
		creatureCount += 1"""
		
		creature = Creature(self.creatureContainer)
		creature.readBestiaryFile("zombie.txt")
		creature.printSelf()
				
class Creature:
	#Health
	#Portrait
	#Stats : STR DEX CON INT WIS CHA
	#AC
	#Attacks
	#Resists, Vulns, Immume, Absorb
	#Movement (type)
	#Name
	#READ a file to load preset
	
	def __init__(self, parent):
		#self.mainContainer = Frame(parent)
		#self.mainContainer.pack()
		self.name = "default"
	
	def readBestiaryFile(self, fileName):
		self.bestiaryFile = open(fileName, "r")
		
		self.name = self.bestiaryFile.readline()
		self.portrait = ImageTk.PhotoImage(Image.open(self.bestiaryFile.readline()))
		self.hp = self.bestiaryFile.readline()
		self.ac = self.bestiaryFile.readline()
		
	def printSelf(self):
		print(self.name + self.hp + self.ac)
		
	def makeImage(self):
		#panel = tk.Label(root, image = img)
		#panel.pack(side = "bottom", fill = "both", expand = "yes")
		self.image = 5

root = Tk()
hobGoblin = HobGoblin(root)
root.wm_attributes("-topmost", 1) 
root.mainloop()