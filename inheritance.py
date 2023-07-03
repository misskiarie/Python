class Animal:
    def __init__(self, name, color):
        self.name = name

    def speak(self):
          raise NotImplementedError("Child classes must implement this method")
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"

class Horse(Animal):
    def speak(self):
        return "Neigh"

dog = Dog("Bosco", "Brown")
print(dog.name)
print(dog.speak())

cat = Cat("Whiskers", "Oreo")
print(cat.name)
print(cat.speak())

object3 = Horse("Zulu", "Blue")

