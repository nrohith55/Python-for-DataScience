class Area_of_rectangle:

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):

        print("Area of Rectangle :" ,self.width*self.height)

object=Area_of_rectangle(10,15)

object.area()