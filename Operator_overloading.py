

class Add:

    def __init__(self,a ,b):

        self.a = a
        self.b = b


    def print_bothvalues(self):

        return self.a ,self.b

    def __str__(self):
       return "({0})".format(self.a)

    def __add__(self, other):
        a = self.a + other.a

        b = self.b + other.b

        c = self.c + other.c

        return (a, b, c)



object1 = Add(10,15)

object2 = Add(1,5)

# object3 = Add(20,25)

#print(object1)


print(object1 + object2)

