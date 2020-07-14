class membership: #class is blue print of the object (properties and method)

     #Constructor

    def __init__(self,fname,lname,age,place,bloodgroup):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.place=place
        self.bloodgroup=bloodgroup

    def fullname(self):
        return self.fname+" "+self.lname

    def city(self):
         return self.place

    def everything(self):
        return self.fname+" "+self.lname,self.place,self.age,self.bloodgroup

var=membership("Rohith","Neelagiriyappa",30,"Mumbai","A+")
var1=membership("Amith","Neelagiriyappa",28,"Delhi","O+")


print(var.fullname())
print(var1.fullname())
print(var.city())
print(var1.everything())