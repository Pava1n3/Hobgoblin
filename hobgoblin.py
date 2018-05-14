#http://thinkingtkinter.sourceforge.net/
from tkinter import *
from PIL import Image, ImageTk

creatureCount = 0
creatureArray = []

class HobGoblin:					     
	def __init__(self, parent):		 
		self.mainContainer = Frame(parent) #Create a container, which stores data but displays nothing
		self.mainContainer.pack()
		self.creatureContainer = Frame(parent)
		self.creatureContainer.pack()
		
		self.makeCreatureButton = Button(self.mainContainer, text="Raise a zombie", background="grey") #Button stored in mainContainer, a 'widget'
		self.makeCreatureButton.pack()
		self.makeCreatureButton.bind("<Button-1>", self.makeCreatureButtonClick)  		
		
	def makeCreatureButtonClick(self, event):	
		global creatureArray
		global creatureCount
		
		creature = Creature(self.creatureContainer, "zombie.txt")
		creatureCount += 1
		creatureArray.append(creature)
		
				
#Creature main class creature with display, data and methods etc.				
class Creature:
	def __init__(self, container, source):
		self.data = CreatureData()
		self.display = CreatureDisplay()
		
		self.data.readBestiaryFile(source)
		self.display.createDisplay(container, self.data)
		self.id = creatureCount
				
class CreatureDisplay:
	def __init__(self):
		pass
		
	def createDisplay(self, container, data):
		labelText = self.createStatBlock(data)
	
		self.label = Label(container, compound=TOP, text=labelText, image=data.portrait)
		self.label.image = data.portrait
		self.label.pack(side=LEFT)
		
	def createStatBlock(self, data):
		return data.name + "\n HP: " + data.hp+ "\n AC: " + data.ac + "\n STR DEX CON INT WIS CHA"
	
class CreatureManager:
	def __init__(self, parent):
		self.parent = parent
		
	def createDestroyButton(self, container): #potentially borked methods
		destroyButton = Button(container, text="Destroy " + str(parent.id), command= lambda : self.destroyCreature())
		destroyButton.bind("<Button-1>", lambda e : self.destroyCreature())
		destroyButton.pack(side=LEFT)
		
	def destroyCreature(self):
		creatureArray[parent.id].destroy() #parent + all children should be deaded
				
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
		#Change all strings/ints to StringVars (IntVars???) so they will update
		self.name = "default"
	
	def readBestiaryFile(self, fileName):
		self.bestiaryFile = open(fileName, "r")
		
		self.name = self.bestiaryFile.readline().rstrip('\n')
		self.portrait = ImageTk.PhotoImage(Image.open(self.bestiaryFile.readline().rstrip('\n')))
		self.hp = self.bestiaryFile.readline().rstrip('\n')
		self.ac = self.bestiaryFile.readline().rstrip('\n')
		
	def printSelf(self):
		print(self.name + self.hp + self.ac)

root = Tk()
hobGoblin = HobGoblin(root)
root.wm_attributes("-topmost", 1) 
root.mainloop()