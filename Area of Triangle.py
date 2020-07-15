class Area_of_Triangle:

    def __init__(self,width,height):
        self.width=width
        self.height=height

    def Area(self):
        print ((self.width*self.height)/2)

obj=Area_of_Triangle(10,15)

obj.Area()