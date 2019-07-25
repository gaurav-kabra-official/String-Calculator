

'''
String Operations
'''

from tkinter import *
from Window import *

class Object():
	frame = Tk()                                                                #as output window
	frame.geometry("1500x1500")
	frame.configure(bg='cyan')
	frame.title("OUTPUT SCREEN")

	'''
	class for o1 and o2
	to perform various logics
	on strings
	'''

	def __init__(self, string, startIdx = 0,endIdx = 0):                        #use of DEFAULT ARGS - compile time polymorphism
		self.string = string
		try:
			self.startIdx = int(startIdx)
			self.endIdx = int(endIdx)
		except:
			print("Could not convert string to integer index")

	'''
	dunder methods
	'''

	def __add__(self,other):
		Label(self.frame,text = "overloaded +").pack()
		'''
		implement + on yourself
		'''
		t = self.string
		for s in other.string:
			self.string += s

		Label(self.frame,text = "RESULT OF + : " + self.string+"\n"+"####################   concat successful    ########################").pack()
		self.string = t                                         # restore original entered value

		

	def __mul__(self,other):
		Label(self.frame,text = "overloaded *").pack()
		'''
		implement * on yourself
		'''
		try:                                                    #use of EXCEPTION HANDLING/other.str may not be a number
			multiplier = int(other.string)
			t = ""
			for num in range(multiplier):
				t += self.string
			Label(self.frame,text = "RESULT OF * : " + t+"\n"+"####################   MULTIPLICATION successful    ########################").pack()
		except:
			Label(self.frame,text = "Second string is not a number\n"+"####################   MULTIPLICATION unsuccessful    ########################").pack()

	def getUpper(self):
		t = ""
		for i in range(len(self.string)):
			if self.string[i]>='a' and self.string[i]<='z':
				lower_ascii = ord(self.string[i])
				upper_ascii = lower_ascii-97+65
				t += chr(upper_ascii)
			else:
				t += self.string[i]
		Label(self.frame,text = "RESULT OF UPPER :"+t+"\n####################   UPPER unsuccessful    ########################").pack()
		

	def getLower(self):
		t = ""
		for i in range(len(self.string)):
			if self.string[i]>='A' and self.string[i]<='Z':
				upper_ascii = ord(self.string[i])
				lower_ascii = upper_ascii-65+97
				t += chr(lower_ascii)
			else:
				t += self.string[i]
		Label(self.frame,text = "RESULT OF LOWER :"+t+"\n####################   LOWER unsuccessful    ########################").pack()


	def getSubstring(self):
		try:
			s = ""
			for i in range(self.startIdx,(self.endIdx)+1):
				s += str(self.string[i])
			Label(self.frame,text = "RESULT OF SUBSTRING :"+s+"\n####################   SUBSTRING OPERATION successful    ########################").pack()
		except:
			Label(self.frame,text = "Index out of bounds!\n####################   SUBSTRING OPERATION unsuccessful    ########################").pack()

	def getCompared(self,other):
		if len(self.string)!=len(other.string):
			Label(self.frame,text = "RESULT OF COMPARING :"+str(False)+"\n####################   COMPARING OPERATION successful    ########################").pack()
		else:
			for i in range(len(self.string)):
				if self.string[i] != other.string[i]:
					Label(self.frame,text = "RESULT OF COMPARING :"+str(False)+"\n################   COMPARING OPERATION successful  ##########################").pack()
					break
			else:
					Label(self.frame,text = "RESULT OF COMPARING :"+str(True)+"\n####################   COMPARING OPERATION successful    ########################").pack()

				
	def getSorted(self):
		letters = [l for l in self.string]
		#sort
		for i in range(len(letters)):
			for j in range(i,len(letters)):
				if letters[i] > letters[j]:
					letters[i], letters[j] = letters[j], letters[i]
		Label(self.frame,text = "RESULT OF SORTING :"+''.join(letters)+"\n####################   SORTING OPERATION successful    ########################").pack()


	def contains(self,other):        
		if other.string in self.string:
			Label(self.frame,text = "RESULT OF CONTAINING: YES\n####################   CONTAINS OPERATION successful    ########################").pack()
		else:
			Label(self.frame,text = "RESULT OF CONTAINING : NO\n####################CONTAINS OPERATION successful    ########################").pack()

	def indexOf(self,other):
		  Label(self.frame,text = "RESULT OF INDEX-OF :"+str(self.string.find(other.string))+"\n####################   INDEX-OF OPERATION successful    ########################").pack()
			
			
   
				
