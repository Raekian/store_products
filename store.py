class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category= category

    def update_price(self, percent_change, is_increased):
        if is_increased:
             self.price += (self.price * percent_change)
        else:
            self.price -=(self.price * percent_change)
        return self

    def print_info(self):
        print(self.name, self.price, self.category)


class Store():
    def __init__(self, name):
        self.name = name
        self.products = [ ]

# I'm being fancy with my name, but this is just appending a Product to a products list
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        print("You are selling the " + self.products[id].name)
        self.products.pop(id)

        # increase the price of each product by percent_increase
    def inflation(self, percent_increase):
                # i refers to the object of "i" which in this instance will be a product
        for i in self.products:
            i.update_price(percent_increase, True)

    # im going to decrease the price of all products that match the provided category by percent_discount
    def set_clearance(self, discount_category, percent_discout):
                # i refers to the object of "i" which in this instance will be a product
        for i in self.products:
            if i.category == discount_category:
                i.update_price(percent_discout, False)

# list all of the current products
    def list_inventory(self):
        # i refers to the object of "i" which in this instance will be a product
        for i in self.products:
            i.print_info()


store1 = Store("Stuff'n Coffee")
pro1 = Product("couch",2000, "furniture")
pro2 = Product("matress", 1000, "furniture")
pro3 = Product("coffe beans", 20, "grocery")

store1.add_product(pro1).add_product(pro2).add_product(pro3)

# store1.list_inventory()
# store1.sell_product(0)
# store1.list_inventory()
# store1.inflation(.10)
store1.list_inventory()
store1.set_clearance("furniture", .10)
store1.list_inventory()

# pro1.update_price(0.02, True)
# print("====================")
# pro1.print_info()
# print("====================")
# pro2.print_info()
# print("====================")
# pro3.print_info()