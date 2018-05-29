from tkinter import *

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
		self.creatureData = {}
	
	def readBestiaryFile(self, fileName):
		self.bestiaryFile = open(fileName, "r")
		
		self.name = self.bestiaryFile.readline().rstrip('\n')
		self.portrait = ImageTk.PhotoImage(Image.open(self.bestiaryFile.readline().rstrip('\n')))
		self.hp = self.bestiaryFile.readline().rstrip('\n')
		self.ac = self.bestiaryFile.readline().rstrip('\n')
		
	def writeData(self, key, data):
		self.creatureData[key] = data
	
	def readData(self, key):
		return self.creatureData[key]
		
	def printSelf(self):
		print(self.name + self.hp + self.ac)