# declare a class and give it name Bike
class Bike:
    # the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    # this is a method we created to help show() the current state of the Bike class OBJECT
    def displayInfo(self):
        print('Bike Price: ' + str(self.price))
        print('Max Speed: ' + str(self.max_speed) + ' mph')
        print("Miles ridden: " + str(self.miles))

    # this is a method we created to show when the Bike Object is being ridden  and increases self.miles
    def ride(self):
        print('Riding ...')
        self.miles += 10
        return self

    # this is a method we created to show when the Bike Object is being reversed ** reverse() ** and increases self.miles
    def reverse(self):
        print('Reversing ...')
        if self.miles <= 0:
            print("You can't have negative miles!")
            self.miles = 0
        else:
            self.miles -= 5
        return self




newBike = Bike("$100", 35)
# print(newBike)
# print(newBike.price)
# print(newBike.max_speed)
# print(newBike.miles)
print(newBike.displayInfo())
# newBike.ride()
print(newBike.miles)
print(newBike.displayInfo())
# newBike.ride()
newBike.reverse()
print(newBike.displayInfo())
