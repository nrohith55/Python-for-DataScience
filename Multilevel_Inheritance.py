class GrandFather:

    def fucn1(self):
        print("This is a  1st Grand Father function")

    def func2(self):
        print("This is a  2nd Grand Father function")


class Father(GrandFather):

    def fucn3(self):
        print("This is a  1st Father function")

    def func4(self):
        print("This is a  2nd Father function")


class Child(Father):

    def fucn5(self):
        print("This is a  1st Child function")

    def func6(self):
        print("This is a  2nd Child function")


ch = Child()

ch.fucn5()

ch.func6()

ch.fucn3()

ch.func4()

ch.fucn1()

ch.func2()