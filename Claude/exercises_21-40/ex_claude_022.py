# inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        print(f"{self.name} says: Woof woof!")
    def __str__(self):
        return f"{self.name} from breed {self.breed}"


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Mocoto", "pomeranian")
cat = Cat("gabriel")

animals = [cat, dog]

for i in range(0, len(animals)):
    animals[i].make_sound()
