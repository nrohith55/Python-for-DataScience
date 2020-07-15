
class Grandfather:

    def Grandfather_class_method(self):

        print("This is a first method of Grandfather class")

    def Grandfather_class_Sec_method(self):

        print("This is a Second method of Grandfather class")

class Father:

    def father_class_method(self):

        print("This is a first method of father class")

    def father_class_Sec_method(self):

        print("This is a Second method of father class")

class Mother:

    def Mother_class_method(self):

        print("This is a first method of Mother class")

    def Mother_class_Sec_method(self):

        print("This is a Second method of Mother class")

class Child(Grandfather, Mother, Father):

    def Child_class_method(self):

        print("This is a first method of Child class")

    def Child_class_sec_method(self):

        print("This is a second method of Child class")

ch = Child()

ch.Grandfather_class_method()

ch.father_class_method()

ch.Mother_class_method()

# ch.Child_class_method()

# ch.Child_class_sec_method()

# ch.Mother_class_method()

# ch.Mother_class_Sec_method()

# ch.father_class_method()

# ch.Grandfather_class_method()





