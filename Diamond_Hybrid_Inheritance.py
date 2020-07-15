class A :

    def class_A_function(self):
        print("This is a Class A Function!!!!!")

    def class_A_Sec_function(self):

        print("This is a class A Second Function !!!!!!")

class B(A) :

    def class_B_function(self):

        print("This is a Class B function")


    def class_B_Sec_function(self):
        print("This is a class Second Function !!!!!!!")


class C(B):

    def class_C_function(self):
        print("This is a class C Function")

    def class_C_Sec_function(self):

        print("This is a class Second Function")

class D(C,B):

    def class_D_function(self):

        print("This is a class D Function ")

    def class_D_Sec_function(self):

        print("This is a class D second Function ")


d = D()

d.class_A_function()