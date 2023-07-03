class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.maxcapacity=capacity
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.maxcapacity)

#create an object
myobj=Magari("Toyota", "blue", 2020, 5)
myobj2=Magari("Mercedes", "black", 2023, 4)
myobj.onyesha()
myobj2.onyesha()