class Laptop:

    laptopCount = 0

    def __init__(self, color, screen, weight):
        self.laptopcolor = color
        self.laptopscreen = screen
        self.laptopweight = weight
        Laptop.laptopCount = Laptop.laptopCount + 1

    def display(self):
        print('laptop of color : ',self.laptopcolor, ',screen : ',self.laptopscreen, ',weight : ',self.laptopweight)
        if(hasattr(self,'size')):
            print('laptop size : ' , self.size)
        else:
            print("laptop size not defined")

    def ShowLaptopCount():
        print(Laptop.laptopCount)

    
laptop1 = Laptop('red','LED',56)
setattr(laptop1,'size' , 15.7)
Laptop.display(laptop1)

laptop2 = Laptop('blue','LCD',42)
Laptop.display(laptop2)

Laptop.ShowLaptopCount()

print("Laptop.__doc__: ", Laptop.__doc__)
print("Laptop.__dict__: ", Laptop.__dict__)
