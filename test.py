#http://thinkingtkinter.sourceforge.net/
from tkinter import *

class MyApp:                         
	def __init__(self, myParent):      
		self.myContainer1 = Frame(myParent) #Create a container, which stores data but displays nothing
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1, text="Click me!", background="red") #Button stored in myContainer1, a 'widget'
		self.button1.pack()
		self.button1.bind("<Button-1>", self.button1Click)  
		
	def button1Click(self, event):      
		self.button1.configure(text="Clicked!")
		self.button2 = Button(self.myContainer1, text="The Child" + str(event.x))
		self.button2.pack(side=LEFT)
		#self.button2.bind("<Button-1>", lamba e: self.destroy())

root = Tk()
myApp = MyApp(root)
root.wm_attributes("-topmost", 1) 
root.mainloop()