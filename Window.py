from tkinter import *
from Object import *
'''
GUI Interaction
'''


class Window(Frame):                                            # inherit from Frame class : SINGLE INHERITANCE

    def __init__(self, master=None):
        Frame.__init__(self, master)                            #calling parent class's ctor                 
        self.master = master                                    #parent window
        self.init_window()
        self.str1 = ""
        self.str2 = ""


    '''
    Name to window, size & Buttons
    '''

    def init_window(self):                              
        self.master.title("String Calculator")                  #name of application
        self.pack(fill = BOTH, expand = 1)                      #maximum size of widget
        entryButton = Button(self, text = "Functionalities", command = self.entryWidget,width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic")
        entryButton.pack()
        aboutButton = Button(self, text = "Info", command = self.dispInfo,width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic")
        aboutButton.pack()
        quitButton = Button(self, text = "LEAVE APP", command = self.client_exit,width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic")
        quitButton.pack()



    def entryWidget(self):
        master = Tk()
        master.configure(background="skyblue")
        master.geometry("500x500")
        master.resizable(False,False)
        master.title("Entry")
        Label(master, text = "String #1",fg="white",bg="skyblue",font = "Helvetica 16 bold italic").grid(row = 0)
        Label(master, text = "String #2",fg="white",bg="skyblue",font = "Helvetica 16 bold italic").grid(row = 1)
        Label(master, text = "start Index*",fg="white",bg="skyblue",font = "Helvetica 16 bold italic").grid(row = 2)
        Label(master, text = "End Index*",fg="white",bg="skyblue",font = "Helvetica 16 bold italic").grid(row = 3)

        self.e1 = Entry(master,width=60)
        self.e2 = Entry(master,width=60)
        self.e3 = Entry(master,width=60)
        self.e4 = Entry(master,width=60)
        self.e1.grid(row = 0, column = 1)
        self.e2.grid(row = 1, column = 1)
        self.e3.grid(row = 2, column = 1)
        self.e4.grid(row = 3, column = 1)

        Button(master, text='+ (CONCAT)', command = self.getConcat, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row=6,column=0)
        Button(master, text='* (REPEAT)', command = self.getMultiplied, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row=6,column=1)
        Button(master,text='SUB-STRING', command = self.getSubstr, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 8,column = 0)
        Button(master,text='UPPER', command = self.getUpper, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 8,column = 1)
        Button(master,text='LOWER', command = self.getLower, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 10,column = 0)
        Button(master,text='SORT ALPHABETICALLY', command = self.getSorted, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 10,column = 1)
        Button(master,text='ARE EQUAL ?', command = self.getCompared, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 12,column = 0)
        Button(master,text='CONTAINS ?', command = self.getContained, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 12,column = 1)
        Button(master,text='Index-Of', command = self.getIndexOf, width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row = 14,column = 0)
        
    
        
        
    def dispInfo(self):
        def client_exit():
            master.destroy()
        master = Tk()
        master.title("Info")
        master.geometry("300x130")
        master.resizable(False,False)
        Label(master,text = "This is string calculator.\n It is developed by \nGaurav Kabra\n2016 ucp 1471\n B(3,4)",width=25,bg = 'black',fg='white',font="Helvetica 10 bold italic").grid(row=0)
        Button(master, text = "Got It!", command = client_exit,width=25,bg = '#a1dbcd',fg='black',font="Helvetica 10 bold italic").grid(row=4,column = 0)

        
    '''
    Functionalities
    '''

    
    def getContained(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)
        o2 = Object(self.str2)
        o1.contains(o2)

    def getIndexOf(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)
        o2 = Object(self.str2)
        o1.indexOf(o2)

    def getConcat(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)
        o2 = Object(self.str2)
        o1+o2

    def getMultiplied(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)
        o2 = Object(self.str2)
        o1*o2

    def getUpper(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)
        o2 = Object(self.str2)
        o1.getUpper()
        o2.getUpper()

    def getLower(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)
        o2 = Object(self.str2)
        o1.getLower()
        o2.getLower()

    def getSorted(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)                                      #only 1 arg passed
        o2 = Object(self.str2)
        o1.getSorted()
        o2.getSorted()

    def getSubstr(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        startIdx = self.e3.get()
        endIdx = self.e4.get()
        o1 = Object(self.str1,startIdx,endIdx)                      #3 args passed
        o2 = Object(self.str2,startIdx,endIdx)
        o1.getSubstring()
        o2.getSubstring()

    def getCompared(self):
        self.str1 = self.e1.get()
        self.str2 = self.e2.get()
        o1 = Object(self.str1)                      #3 args passed
        o2 = Object(self.str2)
        o1.getCompared(o2)
        
    def client_exit(self):
        exit()
