# ------------------------------------------------------------------------------/
#   Assignment: Car
#
#    Objectives:
#       Practice creating a class and making instances from it
#       Practice accessing the methods and attributes of different instances
#
# ------------------------------------------------------------------------------/


class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price >= 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print('Price: $' + str(self.price))
        print('Speed: ' + str(self.speed) + 'mph')
        print('Fuel: ' + str(self.fuel))
        print('Mileage: ' + str(self.mileage) + 'mpg')
        print('Tax: ' + str(self.tax))


newCar1 = Car(10000, 55, "Full", 10)
newCar2 = Car(8000, 45, "Not Full", 7)
newCar3 = Car(22000, 85, "Half Full", 21)
usedCar1 = Car(15000, 65, "Full", 15)
usedCar2 = Car(6000, 35, "Empty", 12)
print(newCar1.display_all())
print(newCar2.display_all())
print(newCar3.display_all())
print(usedCar1.display_all())
print(usedCar2.display_all())
