from tkinter import *
from geometrymanager.addtogrid import AddToGrid as hgrid
from creaturemanager.creaturedata import CreatureData

class SingleFieldWidget():
	def __init__(self, container, labelText, entryDataKey, entryDataType="text", entryWidth=10):
		self.label = SimpleLabel(container, labelText)
		self.entry = SimpleEntry(container, entryDataKey, entryWidth, entryDataType)
		
		#data = CreatureData() testing purposes only
		#data.writeData("Hit Points", 667)
		
	def displayWidget(self, r, c1, c2):
		self.label.displaySelf(r, c1)
		self.entry.displaySelf(r, c2)
		
	def displayLabel(self, r, c):
		self.label.displaySelf(r, c)
		
	def displayEntry(self, r, c):
		self.entry.displaySelf(r, c)
		
	def loadCreature(self, data):
		self.entry.loadCreature(data)		

class SimpleEntry(Entry):
	def __init__(self, container, dataKey, w=10, entryType="text"):
		Entry.__init__(self, container, width=w, validate="key")
		self.validateStrings = {"text": "abcdefghijklmnopqrstuvwxyz", "numerical":"1234567890"}
		self.key = dataKey
		
		validateMethod = self.register(self.validateCommand)
		self.config(vcmd=(validateMethod, entryType, '%d', '%S'))
		
	def displaySelf(self, r, c):
		hgrid.padGrid(self, r, c)
		
	def loadCreature(self, data):
		self.insert(0, data.readData(self.key))
		
	def validateCommand(self, entryType, entryMode, entry):
		if entryMode == 0:
			return 'true'
			
		if entryType == "all":
			return 'true'
		
		if entry in self.validateStrings[entryType]:
			return 'true'
		else:
			return 'false'
			
class SimpleLabel(Label):
	def __init__(self, container, labelText):
		Label.__init__(self, container, text=labelText)
		
	def displaySelf(self, r, c):
		hgrid.padGrid(self, r, c)