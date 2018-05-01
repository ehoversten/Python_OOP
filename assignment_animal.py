# ------------------------------------------------------------------------------/
#   Assignment: Animal
#       Objectives:
#           Practice creating classes that inherit from another class
#           Practice customizing children classes
#           Practice having children classes call methods from the parent class
#
# ------------------------------------------------------------------------------/

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print("Health: " + str(self.health))


# ---- Declare a Dog class that inherits from class Animal

class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        if health > 150:
            self.health = health
        else:
            self.health = 150

    def pet(self):
        self.health = self.health + 5
        return self

# ---- Declare a Dragon class that inherits from class Animal

class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        if health > 170:
            self.health = health
        else:
            self.health = 170

    def fly(self):
        self.health = self.health - 10

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")


# ------------------------------------------------------------------------------/
#
#  Code to Test functionality of Animal class
#
# ------------------------------------------------------------------------------/


testAnimal = Animal("Tom Cat", 50)
testAnimal.displayHealth()
testAnimal.walk().walk().walk().run().run().displayHealth()

aDog = Dog("Marmaduke", 175)
aDog.displayHealth()
aDog.walk().walk().walk().run().run().pet().displayHealth()

aDragon = Dragon("Falcore", 225)
aDragon.displayHealth()

aDog.displayHealth()

secondDog = Dog("Max", 35)
secondDog.displayHealth()
