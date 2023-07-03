class People:
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age
    def onyesha(self):
        print(self.name, self.gender, self.age)
myobj=People("Pira", "Male", 21)
myobj2=People("Joy", "Female", 20)
myobj3=People("Lois", "Female", 50)
myobj.onyesha()
myobj2.onyesha()
myobj3.onyesha()