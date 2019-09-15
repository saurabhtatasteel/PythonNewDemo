# !/usr/bin/python3
from tkinter import * 

class MyGUI:
    
    result = 0   
    param1 = 0
    param2 = 0
    operator = ''

    def __init__(self,myWindow):

        def ButtonHit(btnClicked):

            if(str(btnClicked).isnumeric()):
                if(MyGUI.operator == ''):
                    MyGUI.param1 = int(str(MyGUI.param1) + str(btnClicked))
                    self.resultLabel.configure(text=MyGUI.param1)
                elif (MyGUI.operator != ''):
                    MyGUI.param2 = int(str(MyGUI.param2) + str(btnClicked))
                    self.resultLabel.configure(text=MyGUI.param2)
            else:
                if(btnClicked == "="):
                    if(MyGUI.operator == "+"):
                        MyGUI.result = MyGUI.param1 + MyGUI.param2                        
                    elif(MyGUI.operator == "-"):
                        MyGUI.result = MyGUI.param1 - MyGUI.param2
                    elif(MyGUI.operator == "*"):
                        MyGUI.result = MyGUI.param1 * MyGUI.param2
                    elif(MyGUI.operator == "/"):
                        MyGUI.result = MyGUI.param1 / MyGUI.param2

                    MyGUI.param1 = MyGUI.result
                    MyGUI.param2 = 0
                    MyGUI.operator = ''
                    self.resultLabel.configure(text=MyGUI.result)
                elif(btnClicked == "C"):
                    MyGUI.result = 0   
                    MyGUI.param1 = 0
                    MyGUI.param2 = 0
                    MyGUI.operator = ''
                    self.resultLabel.configure(text=MyGUI.result)
                else:
                    MyGUI.operator = btnClicked       
            
        
        #creating result label
        self.resultLabel = Label(myWindow,text="0", fg="blue",bg="white", width="68", height="5")
        #self.resultLabel.pack(side=TOP)
        self.resultLabel.grid(row=1,columnspan=4)

        #creating C button
        self.clearButton = Button(myWindow,command=lambda:ButtonHit("C"), text = "C",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.clearButton.pack(side = RIGHT)
        self.clearButton.grid(row=5, column=1)

        #creating * button
        self.multiplyButton = Button(myWindow,command=lambda:ButtonHit("*"), text = "*",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.multiplyButton.pack(side = RIGHT)
        self.multiplyButton.grid(row=4, column=3)

        #creating / button
        self.divideButton = Button(myWindow,command=lambda:ButtonHit("/"), text = "/",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.divideButton.pack(side = RIGHT)
        self.divideButton.grid(row=5, column=3)

        #creating + button
        self.addButton = Button(myWindow,command=lambda:ButtonHit("+"), text = "+",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.addButton.pack(side = RIGHT)
        self.addButton.grid(row=2, column=3)

        #creating - button
        self.substractButton = Button(myWindow,command=lambda:ButtonHit("-"), text = "-",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.substractButton.pack(side = RIGHT)
        self.substractButton.grid(row=3, column=3)

        #creating = button
        self.equalsButton = Button(myWindow,command=lambda:ButtonHit("="), text = "=",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.equalsButton.pack(side = RIGHT)
        self.equalsButton.grid(row=5, column=2)         

        #creating 1 button
        self.oneButton = Button(myWindow,command=lambda:ButtonHit(1), text = "1",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.oneButton.pack(side = RIGHT)
        self.oneButton.grid(row=2, column=0)

        #creating 2 button
        self.twoButton = Button(myWindow,command=lambda:ButtonHit(2), text = "2",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.twoButton.pack(side = RIGHT)
        self.twoButton.grid(row=2, column=1)

        #creating 3 button
        self.threeButton = Button(myWindow,command=lambda:ButtonHit(3), text = "3",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.threeButton.pack(side = RIGHT)
        self.threeButton.grid(row=2, column=2)

        #creating 4 button
        self.fourButton = Button(myWindow,command=lambda:ButtonHit(4), text = "4",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.fourButton.pack(side = RIGHT)
        self.fourButton.grid(row=3, column=0)

        #creating 5 button
        self.fiveButton = Button(myWindow,command=lambda:ButtonHit(5), text = "5",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.fiveButton.pack(side = RIGHT)
        self.fiveButton.grid(row=3, column=1) 

        #creating 6 button
        self.sixButton = Button(myWindow,command=lambda:ButtonHit(6), text = "6",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.sixButton.pack(side = RIGHT)
        self.sixButton.grid(row=3, column=2)

        #creating 7 button
        self.sevenButton = Button(myWindow,command=lambda:ButtonHit(7), text = "7",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.sevenButton.pack(side = RIGHT)
        self.sevenButton.grid(row=4, column=0) 

        #creating 8 button
        self.eightButton = Button(myWindow,command=lambda:ButtonHit(8), text = "8",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.eightButton.pack(side = RIGHT)
        self.eightButton.grid(row=4, column=1)

        #creating 9 button
        self.nineButton = Button(myWindow,command=lambda:ButtonHit(9), text = "9",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.nineButton.pack(side = RIGHT)
        self.nineButton.grid(row=4, column=2) 

        #creating 0 button
        self.zeroButton = Button(myWindow,command=lambda:ButtonHit(0), text = "0",font=8, fg = "black", width="12", height="5", bg="silver") 
        #self.zeroButton.pack(side = RIGHT)
        self.zeroButton.grid(row=5, column=0) 
        
        
    

#creating the application main window.
myWindow = Tk()
myWindow.geometry("472x498")
myWindow.resizable(0,0)
mygui = MyGUI(myWindow)
myWindow.title("Simple Calculator")
#Entering the event main loop
myWindow.mainloop() 