class Process:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    def __init__(self, product_name, product_cost):
        self.__product_name = product_name
        self.__product_cost = product_cost


    @property
    def product_name(self):
        return str(self.__product_name).title()

    @property
    def prodcut_price(self):
        return str(self.__product_cost).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__first_name = value
        else:
            raise Exception("Product name cannot be numbers")

#---methods---------#
    def __str__(self):
        return self.__product_name
