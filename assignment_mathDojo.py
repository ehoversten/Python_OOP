# ------------------------------------------------------------------------------/
#   Assignment: MathDojo
#       Objectives:
#           Practice creating a class and creating new instances
#           Practice chaining methods
#           Practice writing flexible functions that can take a variable number of arguments
#
# ------------------------------------------------------------------------------/


# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.


class MathDojo(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2
