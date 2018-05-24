from tkinter import *

class AddToGrid:		
	def __init__(self):
		pass
		
	def doGrid(objectg, gRow=0, gColumn=0, gSticky="nsew", gColumnspan=1, doConfig="false", gWeight=1, gPadx=0, gPady=0):
		objectg.grid(row=gRow, column=gColumn, sticky=gSticky, columnspan=gColumnspan, padx=gPadx, pady=gPady)
		if(doConfig):
			objectg.grid_columnconfigure(gColumn, weight=gWeight)
			objectg.grid_rowconfigure(gRow, weight=gWeight)
	
	def padGrid(objectg, gRow=0, gColumn=0, gPadx=5, gPady=5, gSticky="nsew", gColumnspan=1, doConfig="false", gWeight=1):
		AddToGrid.doGrid(objectg, gRow, gColumn, gSticky, gColumnspan, doConfig, gWeight, gPadx, gPady)
	
	def ConfigureColumns(self, container, nrOfColumns=10, cWeight=1):
		for col in range(nrOfColumns):
			container.grid_columnconfigure(col, weight=cWeight)
			
	def ConfigureRows(self, container, nrOfRows=10, rWeight=1):
		for row in range(nrOfRows):
			container.grid_rowconfigure(row, weight=rWeight)
	
	def ConfigureRowsAndColumns(self, container, nrOfColumnsAndRows=10, rcWeight=1):
		self.ConfigureColumns(container, nrOfColumnsAndRows, rcWeight)
		self.ConfigureRows(container, nrOfColumnsAndRows, rcWeight)
		
	