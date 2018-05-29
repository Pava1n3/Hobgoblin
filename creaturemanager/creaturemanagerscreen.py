from tkinter import *
from geometrymanager.addtogrid import AddToGrid as hGrid
from creaturemanager.creaturemanagerwidgets import *
from creaturemanager.creaturemanagerwidgetsbase import *
from creaturemanager.creaturedata import CreatureData

class CreatureManagerScreen(Frame):
	def __init__(self, container, controller):
		Frame.__init__(self, container, bg="#00FF96") #init takes a master, which is container which is HobGoblin.mainContainer
		
		root = controller.getRoot()
		self.createMenuBar(root)
		self.creatureData = CreatureData()
		self.createCreatureManagerWidgets()
		self.gridCreatureManagerWidgets()
		
		#Some columnial configuring. This centers the stat block in the window
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(100, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(100, weight=1)
		
	def createMenuBar(self, root):
		self.creatureManagerMenuBar = Menu(root)
		self.creatureManagerMenuBar.add_command(label="New")
		self.creatureManagerMenuBar.add_command(label="Open")
		self.creatureManagerMenuBar.add_command(label="Save")
		self.creatureManagerMenuBar.add_separator()
		self.creatureManagerMenuBar.add_command(label="Main Menu")
		
	def createCreatureManagerWidgets(self):
		self.nameWidget =  SingleFieldWidget(self, "Name", "name", "all", entryWidth=10)
		self.challengeRatingWidget =  SingleFieldWidget(self, "Challenge Rating", "cr", "numerical", entryWidth=2)
	
		self.alignmentLabel = Label(self, text="Alignment")
		self.alignmentEntry = Entry(self)
		
		self.typeTagsLabel = Label(self, text="Type dropdown")
		self.typeTagsEntry = Entry(self)
		
		self.languageLabel = Label(self, text= "Languages")
		
		self.sensesLabel = Label(self, text="Senses", anchor="w")
		self.sensesEntry = Entry(self)
		
		self.portrait = Frame(self, bg="cyan", width=25, height=25)
		
		#========================================================#
		
		self.statisticsSeparator = Label(self, text="Statistics", font="Serif", height=3, bg="#00FF96")
		
		self.savesLabel = Label(self, text="Saving Throws")
		
		self.conditionBar = Label(self, text="Condition Immunities")
		
		self.weakAndResistBar = Label(self, text="Weaknesses & Resistances, buttons for res/vuln/imm/abs", anchor="w")
		self.weakAndResistEntry = Label(self, text="Type in bar, autocomplete to dmg types")
		
		self.hitPointWidget = SingleFieldWidget(self, "Hit Points", "hp", "numerical", entryWidth=4)
		self.armorClassWidget = SingleFieldWidget(self, "Armor Class", "ac", "numerical", entryWidth=4)
		
		self.movementTitleBar = Label(self, text="Movement", anchor="w")
		self.movementAddMovementButton = Button(self, text="Add Movement Type")
		
		self.statsBar = Label(self, text="STR  DEX  CON  INT  WIS  CHA")
		
		#========================================================#
		
		self.techniqueSeparator = Label(self, text="Techniques", font="Serif", height=3, bg="#00FF96")
		
		self.passiveLabel = Label(self, text="Passives")
		
		self.actionsLabel = Label(self, text="Actions", anchor="w")
		self.actionsEntry = Frame(self, bg="#C41F3B", width=150, height=75)
		
		
		#Tag system:
		#	Type
		#	Language
		#	Weaknesses
		#	Resistances
		#	Immunities
		#	Absorbs
		#	Vulnerabilities
		#	Saving Throws
		
		#Single Entry (text)
		#	Name
		#	Hit Points
		#	CR
		
		#Add from option (dropdown?)
		#	Movement
		#	Senses
		#	Alignment
		
		#TBD
		#	Actions
		#	Passives
		
	def gridCreatureManagerWidgets(self):
		self.nameWidget.displayWidget(1, 1, 2)
		
		hGrid.padGrid(self.typeTagsLabel, 2, 1)
		hGrid.padGrid(self.typeTagsEntry, 2, 2)
	
		hGrid.padGrid(self.alignmentLabel, 2, 4)
		hGrid.padGrid(self.alignmentEntry, 2, 5)

		hGrid.padGrid(self.languageLabel, 3, 1)
		
		self.challengeRatingWidget.displayWidget(4, 1, 2)
		
		hGrid.padGrid(self.sensesLabel, 5, 1)
		hGrid.padGrid(self.sensesEntry, 5, 2)
	
		#========================================================#
	
		hGrid.doGrid(self.statisticsSeparator, 6, 1, "nsew", 6)
	
		self.hitPointWidget.displayWidget(7, 1, 2)
		self.armorClassWidget.displayWidget(7, 4, 5)
		
		hGrid.padGrid(self.movementTitleBar, 8, 1, 3, 3, "nsew", 6) #clmnspn 5
		hGrid.padGrid(self.movementAddMovementButton, 8, 6)
		
		hGrid.padGrid(self.savesLabel, 9, 1)
		
		hGrid.padGrid(self.conditionBar, 10, 1, 3, 3, "nsew", 6)
		
		hGrid.padGrid(self.weakAndResistBar, 11, 1, 3, 3, "nsew", 6)
		hGrid.padGrid(self.weakAndResistEntry, 11, 5)
		
		#========================================================#
		
		hGrid.doGrid(self.techniqueSeparator, 12, 1, "nsew", 6)
		
		hGrid.padGrid(self.passiveLabel, 13, 1, 3, 3, "nsew", 6)
		
		hGrid.padGrid(self.actionsLabel, 14, 1, 3, 3, "nsew", 6)
		hGrid.padGrid(self.actionsEntry, 15, 1, 1, 1, "nsew", 6)
		
	def handlePageSwitch(self, root):
		root.config(menu=self.creatureManagerMenuBar)

