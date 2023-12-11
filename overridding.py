 
class person:
    def printtype(self):
        print("person")

class customer(person):
    def printtype(self):
        print("customer")
    

class employee(person):
    def printtype(self):
        print("employee")
   
    
class doctor(person):
    def printtype(self):
        print("doctor")


p = person()
c = customer()
e = employee()
d = doctor()

p.printtype()
c.printtype()
e.printtype()
d.printtype()

