class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Roar!")

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Ooh Ooh Ahh Ahh!")

lion = Lion("Simba", 5)
monkey = Monkey("Rafiki", 10)

print(lion.name)
monkey.make_sound()