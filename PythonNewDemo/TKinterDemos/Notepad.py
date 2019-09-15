from tkinter import *
import tkinter as tk
import sys
from tkinter import filedialog
import os
import win32clipboard
import tkinter.messagebox

class MyNotepad:
    
    def __init__(self):        

        #creates a new my notepad file
        def NewFile():
            myNewNotePad = MyNotepad()

        def OpenFile(mytextbox,myWindow):
            openedFileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("All files","*.*")))
            openFile = open(openedFileName, "r")
            myfileData = openFile.read()
            openFile.close()
            mytextbox.delete('1.0', END)
            mytextbox.insert(tk.END, myfileData)
            myWindow.title(openedFileName)

        def SaveFile(mytextbox):
            saveFileName =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
            if saveFileName is None or saveFileName=='': # asksaveasfile return `None` if dialog closed with "cancel".
                return
            text2save = str(mytextbox.get(1.0, END)) # starts from `1.0`, not `0.0`
            openFile = open(saveFileName, "w")
            openFile.write(text2save)
            openFile.close() # `()` was missing.

        def SaveAsFile(mytextbox):
            saveFileName =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
            if saveFileName is None or saveFileName=='': # asksaveasfile return `None` if dialog closed with "cancel".
                return
            text2save = str(mytextbox.get(1.0, END)) # starts from `1.0`, not `0.0`
            openFile = open(saveFileName, "w")
            openFile.write(text2save)
            openFile.close() # `()` was missing.

        def AboutNotepad(self):
            aboutWindow=Toplevel(self.master)
            aboutWindow.geometry("500x412")
            aboutWindow.resizable(0,0)
            aboutWindow.title("About My Notepad")
            okButton = Button(aboutWindow, text = "OK", command =lambda:aboutWindow.destroy())    
            okButton.place(x=375,y=350)  
            p1 = PhotoImage(file = 'C:\\Users\\Saurabh\\Desktop\\MyNotepadIcon.PNG')
            aboutWindow.iconphoto(False, p1)
            aboutWindow.configure(bg = "silver")
            aboutWindow.grab_set()
            w = Label(aboutWindow, text='Windows 10')
            w.pack()

        def Copy(r,text):
            r.clipboard_clear()
            copiedText = text.selection_get()
            r.clipboard_append(copiedText)

        def Cut(r, text):
            r.clipboard_clear()
            cutText = text.selection_get()
            r.clipboard_append(cutText)
            text.delete('1.0', END)
            text.update()

        def Paste(text):
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            myIndex = text.index(tk.INSERT)
            text.insert(myIndex, data)

        def Delete(text):            
            text.delete("sel.first", "sel.last")
            text.update()

        def SelectAll(text):
            text.tag_add(SEL, "1.0", END)
            text.mark_set(INSERT, "1.0")
            text.see(INSERT)
            return 'break'

        def FindNext(text, entry):
                allText = text.get(1.0, END)
                findText = entry.get()
                lenFindText = len(findText)
                startIndexCursor = text.index(tkinter.INSERT)
                dotIndex = startIndexCursor.find(".", 0, len(startIndexCursor))
                startIndexForText = str(startIndexCursor)[dotIndex+1 : len(startIndexCursor)]
                firstIndex = allText.find(findText, int(startIndexForText), len(allText))
                startRange = "1." + str(firstIndex)   
                endRange = "1." + str(firstIndex + lenFindText) 
                text.tag_add(SEL, startRange, endRange)
                text.focus_set()
                text.mark_set("insert", "%d.%d" % (1, firstIndex + lenFindText))
                test = 'test'

        def Replace(self):
            replaceWindow=Toplevel(self.master)
            replaceWindow.geometry("400x200")
            replaceWindow.resizable(0,0)
            replaceWindow.title("Replace")
            L1 = Label(replaceWindow, text="Find")
            L1.grid(row=0, column=0)
            L2 = Label(replaceWindow, text="Replace With")
            L2.grid(row=1, column=0)
            E1 = Entry(replaceWindow, bd =3)
            E1.grid(row=0, column=1)
            E2 = Entry(replaceWindow, bd =3)
            E2.grid(row=1, column=1)            

            #returning total row and column count in the grid of replace window.
            col_count, row_count = replaceWindow.grid_size()
            for col in range(col_count):
                replaceWindow.grid_columnconfigure(col, minsize=40)

            for row in range(row_count):
                replaceWindow.grid_rowconfigure(row, minsize=40)
              
            frame = Frame(replaceWindow) 
            
            findNextButton = Button(frame, text = "Find Next", command=lambda:FindNext(text, E1))
            findNextButton.pack(side = LEFT)
            replaceButton= Button(frame, text = "Replace", command=Replace)
            replaceButton.pack(side = LEFT)
            cancelButton= Button(frame, text = "Cancel", command=lambda:replaceWindow.destroy())
            cancelButton.pack(side = LEFT)
            frame.grid(row=2, column=0, columnspan=3)


        def ExitFile(openedWindow):
            #if tkMessageBox.askokcancel("Quit", "You want to quit now? *sniff*"): 
            openedWindow.destroy()
            #sys.exit(1)

        #def WindowCallback(mainWindow):
        #    if(aboutWindowOpened):
        #        #focus back to about window
        #        mainWindow.after(1, lambda: mainWindow.focus_force())

                

        #constructor code below

        myWindow = tk.Tk()

        

        yscrollbar = tk.Scrollbar(myWindow)  
        yscrollbar.grid(row=0, column=1,rowspan=2, sticky="nsew")

        xscrollbar = tk.Scrollbar(myWindow, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, columnspan=2, sticky="nsew")

        text = tk.Text(myWindow, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,fg = "black",bg="white")
        text.grid(row=0, column=0, sticky=tk.NSEW)

        #myWindow.bind('<Control-c>', lambda:Copy(myWindow,text))

        xscrollbar.config(command=text.xview)
        yscrollbar.config(command=text.yview)

        myWindow.columnconfigure(0, weight=1)
        myWindow.columnconfigure(1, weight=0)
        myWindow.rowconfigure(0, weight=1)
        myWindow.rowconfigure(1, weight=0)

        menubar = tk.Menu(myWindow)  
        file = tk.Menu(menubar, tearoff=0)  
        file.add_command(label="New", command=NewFile) 
        file.add_command(label="Open", command=lambda:OpenFile(text,myWindow))  
        file.add_command(label="Save", command=lambda:SaveFile(text))  
        file.add_command(label="Save as...", command=lambda:SaveAsFile(text)) 

        file.add_separator()  
  
        file.add_command(label="Exit", command=lambda:ExitFile(myWindow))

        menubar.add_cascade(label="File", menu=file) 
        
        edit = tk.Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
  
        edit.add_separator()  
  
        edit.add_command(label="Cut", command=lambda:Cut(myWindow,text)) 
        edit.add_command(label="Copy", command=lambda:Copy(myWindow,text))
        edit.add_command(label="Paste", command = lambda:Paste(text))  
        edit.add_command(label="Delete", command=lambda:Delete(text))  
        edit.add_command(label="Select All", command=lambda:SelectAll(text)) 
        
        edit.add_separator()
        edit.add_command(label="Replace", command=lambda:Replace(myWindow))
        edit.add_command(label="Find")
        edit.add_command(label="Find Next")
        menubar.add_cascade(label="Edit", menu=edit)  

        view = tk.Menu(menubar, tearoff=0)  
        view.add_command(label="Status Bar")  
        menubar.add_cascade(label="View", menu=view)  

        help = tk.Menu(menubar, tearoff=0)  
        help.add_command(label="About", command=lambda:AboutNotepad(myWindow))  
        menubar.add_cascade(label="Help", menu=help)  
        myWindow.config(menu=menubar) 

        myWindow.geometry("500x412")
        p1 = PhotoImage(file = 'C:\\Users\\Saurabh\\Desktop\\MyNotepadIcon.PNG')
        myWindow.iconphoto(False, p1)
        myWindow.title("My Notepad")
        myWindow.configure(bg = "white") 
        # bind event to window click to handle anything
        #myWindow.bind("<Button-1>", lambda:WindowCallback(myWindow))        
        myWindow.mainloop()    



#Let's launch the notepad by default when this application is run
myNotepad = MyNotepad()


