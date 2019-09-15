from openpyxl import *
from tkinter import *
class MyGUI:

    wb = load_workbook('C:\Trials\Python Demos\TKinter\RF.xlsx')

    def __init__(self,myWindow):
        MyGUI.sheet = MyGUI.wb.active 

    def excel(self): 
        MyGUI.sheet.column_dimensions['A'].width = 30
        MyGUI.sheet.column_dimensions['B'].width = 10
        MyGUI.sheet.column_dimensions['C'].width = 10
        MyGUI.sheet.column_dimensions['D'].width = 20
        MyGUI.sheet.column_dimensions['E'].width = 20
        MyGUI.sheet.column_dimensions['F'].width = 40
        MyGUI.sheet.column_dimensions['G'].width = 50


        MyGUI.sheet.cell(row=1, column=1).value = "Name"
        MyGUI.sheet.cell(row=1, column=2).value = "Course"
        MyGUI.sheet.cell(row=1, column=3).value = "Semester"
        MyGUI.sheet.cell(row=1, column=4).value = "Form Number"
        MyGUI.sheet.cell(row=1, column=5).value = "Contact Number"
        MyGUI.sheet.cell(row=1, column=6).value = "Email id"
        MyGUI.sheet.cell(row=1, column=7).value = "Address"


myWindow = Tk()
myWindow.geometry("472x600")
myWindow.resizable(0,0)
mygui = MyGUI(myWindow)
myWindow.title("Registration Form")
myWindow.configure(bg = "silver")



heading = Label(myWindow, text="Form", bg="light green") 
name = Label(myWindow, text="Name", bg="light green") 
course = Label(myWindow, text="Course", bg="light green")
sem = Label(myWindow, text="Semester", bg="light green")
form_no = Label(myWindow, text="Form No.", bg="light green") 
contact_no = Label(myWindow, text="Contact No.", bg="light green")
email_id = Label(myWindow, text="Email id", bg="light green") 
address = Label(myWindow, text="Address", bg="light green") 

heading.grid(row=0, column=1) 
name.grid(row=1, column=0) 
course.grid(row=2, column=0) 
sem.grid(row=3, column=0) 
form_no.grid(row=4, column=0) 
contact_no.grid(row=5, column=0) 
email_id.grid(row=6, column=0) 
address.grid(row=7, column=0)

mygui.excel() 

#Entering the event main loop
myWindow.mainloop()


