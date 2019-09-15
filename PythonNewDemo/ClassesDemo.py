class Employee:
    
    empCount = 0

    def __init__(self, name, salary):
        self.EmployeeName = name
        self.EmployeeSalary = salary
        Employee.empCount += 1

    def displayCount():
        print("Total Employee : ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.EmployeeName, ", Salary : ", self.EmployeeSalary)



