class A:

    def func1(self):
        print("Class A 1st function ")

    def func2(self):
        print("Class A 2nd function ")

    def func3(self):
        print("Class A 3rd function ")



class B(A):

    def func4(self):
        print("Class B 1st function ")

    def func5(self):
        print("Class B 2nd function ")

    def func6(self):
        print("Class C 3rd function ")


object=B()

object.func1()