# ------------------------------------------------------------------------------/
#   Assignment: Animal
#       Objectives:
#           Practice creating classes that inherit from another class
#           Practice customizing children classes
#           Practice having children classes call methods from the parent class
#
# ------------------------------------------------------------------------------/

class Animal(object):
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



# ------------------------------------------------------------------------------/
#  Code to Test functionality of Animal class

testAnimal = Animal("Tom Cat", 50)
testAnimal.displayHealth()
testAnimal.walk().walk().walk().run().run().displayHealth()

