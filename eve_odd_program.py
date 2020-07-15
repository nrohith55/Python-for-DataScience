class Even_odd:

#Constructor
    def __init__(self,num):
        self.num=num
#Regular or Instance method
    def eve_odd(self):
        for i in self.num:
            if i%2 == 0:
                print(i,"Number is even")
            else:
                print(i,"Number is odd")

    def eve(self):
        for i in self.num:
            if i%2==0:
                print(i,"Number is even")

    def odd(self):
        for i in self.num:
            if i%2 != 0:
                print(i,"Number is odd")

#Creating object
obj=Even_odd([1,2,3,4,5,6,7,8,9,10,0])

obj.eve_odd()

obj.eve()

obj.odd()