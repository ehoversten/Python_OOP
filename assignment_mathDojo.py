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
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def add(self, num1=None, num2=None):
        temp = 0
        if num1 is None:
            self.num1 = 0
        else:
            self.num1 = num1
        if num2 is None:
            self.num2 = 0
        else:
            self.num2 = num2
        temp = self.num1 + self.num2
        print(str(self.num1) + ' + ' + str(self.num2))
        print('Result: ' + str(temp))
        self.result = self.result + temp
        return self

    def subtract(self, num1=None, num2=None):
        temp = 0
        if num1 is None:
            self.num1 = 0
        else:
            self.num1 = num1
        if num2 is None:
            self.num2 = 0
        else:
            self.num2 = num2
        temp = self.num1 + self.num2
        print(str(self.num1) + ' + ' + str(self.num2))
        print('Result: ' + str(temp))
        self.result = self.result - temp
        return self

    def final(self):
        print("Final Result = " + str(self.result))
        return self


md = MathDojo()
md.add(2).add(2, 5).subtract(3, 2).result
print(md.final())