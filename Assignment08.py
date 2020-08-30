# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <LouisYencken>,<8/26/2020>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "products.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  #
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strproduct = ""  # Captures the user task data
strcost = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:

    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <LouisYencken>,<8/29/2020>,Modified code to complete assignment 8
    """

    def __init__(self, product, cost):
        self.__product__ = product
        self.__cost__ = cost

    @property
    def product(self):
        return str(self.__product).title()

    @property
    def __product(self):
        return str(self.__product).title()

    @staticmethod
    def product_name(self, product):
        if str(product).isnumeric() == False:
            self.__product__ = product
        else:
            raise Exception("Product name cannot be numbers")

        # ---methods---------#
    def __str__(self):
        return self.__product
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  #clear current data



        file = open(strFileName, 'r')
        for line in file:
            product, cost = line.split(",")
            row = {"Item": product.strip(), "Cost": cost.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_product_to_list(product, cost, list_of_rows):
        """ Adds product from input to the list of dictionary rows
                :param product: (string) with name of product:
                :param cost: (string) with priority of product:
                :param list_of_rows: (list) you want filled with additional product:
                :return: (list) of dictionary rows
        """
        dicRow = {"Item": product.strip(), "Cost": cost.strip()}
        list_of_rows.append(dicRow)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_product_from_list(product, list_of_rows):
        """ Removes product from input from the list of dictionary rows
            :param product: (string) with name of product:
            :param list_of_rows: (list) you want product removed from:
            :return: (list) of dictionary rows
        """
        bool_list = False
        for dicRow in list_of_rows:
            if dicRow["Item"] == product:
                list_of_rows.remove(dicRow)
                bool_list = True
        if bool_list == False:
            print("cannot find product")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from list of dictionary rows to file
            :param file_name: (string) with name of file:
            :param list_of_rows: (list) you want added to text file:
            :return: (list) of dictionary rows
        """
        objFile = open(file_name, 'w')
        for line in list_of_rows:
            objFile.write(line["Item"] + ',' + line["Cost"] + '\n')
        objFile.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output product """

    @staticmethod
    def print_menu_product():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Remove an existing Product
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        """ Shows the current products in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current  products are: *******")
        for dicRow in list_of_rows:
            print(dicRow["Item"] + " (" + dicRow["Cost"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_cost():

        product = str(input("What Item is to be added: ")).lower().strip()
        cost = str(input("What is the Cost: ")).lower().strip()
        return product, cost

    @staticmethod
    def input_product_to_remove():

        product = str(input("What product do you want removed: ")).lower().strip()
        return product


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_products_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_product()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new product
        product, cost = IO.input_new_product_and_cost()
        lstTable, strStatus = Processor.add_product_to_list(product, cost, lstTable)
        product = Processor.product_name
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing prouct
        product = IO.input_product_to_remove()
        lstTable, strStatus = Processor.remove_product_from_list(product, lstTable)

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Is this really a good idea? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        strChoice = IO.input_yes_no_choice("ensure you have saved before exiting. do you still want to exit (y/n) - ")
        if strChoice.lower() == 'y':
            print("Adios!")
            exit()  # and Exit
        else:
            IO.input_press_to_continue("ok back to the menu!")
        continue  # to show the menu