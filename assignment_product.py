# ------------------------------------------------------------------------------/
#   Assignment: Product
#       Objectives:
#           Practice creating a class and making instances from it
#           Practice accessing the methods and attributes of different instances
#           Practice altering an instance's attributes
#
# ------------------------------------------------------------------------------/

class Product:
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        if self.status == 'sold':
            print('Sorry, Item is not currently in stock')
        else:
            self.status = "sold"
        return self

    def addTax(self, tax):
        self.price = self.price + (self.price * tax)
        return self


    def returnProduct(self, reason_for_return):
        if reason_for_return == "in box":
            self.status = "for sale"
        elif reason_for_return == 'opened':
            self.status = 'used'
            self.price = self.price - (self.price * 0.2)
        elif reason_for_return == 'defective':
            self.status = 'defective'
            self.price = 0
        return self

    def show(self):
        print('Item Name: ' + str(self.item_name))
        print('Price: $' + str(self.price))
        print('Brand: ' + str(self.brand))
        print('Weight: ' + str(self.weight) + 'oz')
        print('Status: ' + str(self.status))



# ------------------------------------------------------------------------------/
#
#       Sample code for testing
#
# ------------------------------------------------------------------------------/

# firstProduct = Product(25, 'Batman T-Shirt', 500, 'Target', 'for sale')
# print(firstProduct.show())
# firstProduct.addTax(0.15).sell()
# firstProduct.sell()
# print(firstProduct.show())
#
# thirdProduct = Product(45, 'Desk Lamp', 500, 'Target', 'used')
# print(thirdProduct.show())
# thirdProduct.addTax(0.12)
# print(thirdProduct.show())
#
#
# secondProduct = Product(2500, 'TV', 5000000, 'Target', 'for sale')
# print(secondProduct.show())
# secondProduct.returnProduct('defective')
# print(secondProduct.show())
#
#
# fourthProduct = Product(4.50, 'Toothpaste', 500, 'Target', 'for sale')
# print(fourthProduct.show())