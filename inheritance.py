class Person:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname   
   
    def printname(self):
        print(self.firstname, self.lastname)

class Name(Person): #Child class p
    pass
x = Name("Christian", "Cruz")
x.printname()



