class Area_of_circle:

    def __init__(self,pie,radius):
        self.pie=3.14
        self.radius=radius

    def area(self):
        print(self.pie*self.radius*self.radius)

object=Area_of_circle(3.14,8)

object.area()