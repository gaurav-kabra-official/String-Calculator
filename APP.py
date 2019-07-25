'''
@author Gaurav Kabra
2 April 2019
uses - (1) Encapsulation
        (2) Inheritance
        (3) Exception Handling
        (4) Operator Overloading
        (5) Default Arguments
        (6) Compile time polymorphism - function overloading
        (7) GUI
MAJOR OOPs Concepts
'''

from tkinter import *
from Window import *
from Object import *

if __name__ == "__main__":
	root = Tk()
	app = Window(root)     #instance of root window
	root.geometry("500x100")
	root.resizable(False, False)
	app.configure(background="#a1dbcd") 
	root.mainloop()
