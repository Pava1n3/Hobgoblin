#http://thinkingtkinter.sourceforge.net/
from tkinter import *
from PIL import Image

creatureCount = 0
creatureArray = []

class HobGoblin:					     
	def __init__(self, parent):		 
		self.mainContainer = Frame(parent) #Create a container, which stores data but displays nothing
		self.mainContainer.pack()
		self.creatureContainer = Frame(parent)
		self.creatureContainer.pack()
		
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
		
		creature = Creature(self.creatureContainer, "zombie.txt")
		
				
#Creature main class creature with display, data and methods etc.				
class Creature:
	def __init__(self, container, source):
		self.data = CreatureData()
		self.display = CreatureDisplay()
		
		self.data.readBestiaryFile(source)
		self.display.createDisplay(container, self.data)
				
class CreatureDisplay:
	def __init__(self):
		pass
		
	def createDisplay(self, container, data):
		self.label = Label(container, text=data.name)
		self.label.pack(side=LEFT)
	
				
class CreatureData:
	#Health
	#Portrait
	#Stats : STR DEX CON INT WIS CHA
	#AC
	#Attacks
	#Resists, Vulns, Immume, Absorb
	#Movement (type)
	#Name
	#READ a file to load preset
	
	def __init__(self):
		self.name = "default"
	
	def readBestiaryFile(self, fileName):
		self.bestiaryFile = open(fileName, "r")
		
		self.name = self.bestiaryFile.readline().rstrip('\n')
		self.portrait = Image.open(self.bestiaryFile.readline().rstrip('\n')) 
		self.hp = self.bestiaryFile.readline().rstrip('\n')
		self.ac = self.bestiaryFile.readline().rstrip('\n')
		
	def printSelf(self):
		print(self.name + self.hp + self.ac)

root = Tk()
hobGoblin = HobGoblin(root)
root.wm_attributes("-topmost", 1) 
root.mainloop()