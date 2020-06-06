# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# AGibbs, 6/6/2020, Completed todo sections in script
# <Your Name>,<Today's Date>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'C:\_PythonClass\Assignment08\products.txt'
list_of_product_objects = []
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions


class Product (object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AGibbs,6/6/2020,Modified code to complete assignment 8
    """

    # --Constructor--
    def __init__(self, product_name, product_price):
        # --Attributes--
        self.__product_name = product_name
        self.__product_price = product_price

    # --Properties--
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value


    @property
    def product_price(self):
        return float(self.__product_price)


    @product_price.setter
    def product_price(self, value):
        self.__product_price = value



# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        write_data_to_file(strFileName, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AGibbs,6/6/2020,Modified code to complete assignment 8
    """

    @staticmethod
    def write_data_to_file(strFileName, list_of_product_objects):
        """ writes list of dictionary rows to .txt file
            :param strFileName: (string) with name of file:
            :param list_of_product_objects: (list) you want appended with file data:
            :return: list_of_product_objects: (list) of rows
        """
        objFile = open(strFileName, 'w')
        for row in list_of_product_objects:
            objFile.write(row['Product'] + ',' + str(row['Price']) + '\n')  # \n important for newline in txt file
        objFile.close()
        return list_of_product_objects

    @staticmethod
    def read_data_from_file(strFileName, list_of_product_objects):
        """ Reads data from a file into a list of dictionary rows
            :param strFileName: (string) with name of file:
            :param list_of_product_objects: (list) you want filled with file data:
            :return: list_of_product_objects: (list) of rows
        """
        list_of_product_objects.clear()  # clear current data
        file = open(strFileName, "r")
        for line in file:
            product, price = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_product_objects.append(row)
        file.close()
        return list_of_product_objects,

    @staticmethod
    def add_data_to_list(product_name, product_price, list_of_product_objects):
        """ Adds data to list of dictionary rows
            :param product_name: (string) from user input:
            :param product_price: (string) from user input:
            :param list_of_product_objects: (list) you want appended with file data:
            :return: list_of_product_objects: (list) of dictionary rows
        """
        row = {'Product': product_name, 'Price': product_price}
        list_of_product_objects.append(row)  # appends lstTable with new entries
        return list_of_product_objects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Gets input from user and presents data:

       methods:
       print_menu_Tasks():
       input_menu_choice():
       print_current_Products_in_list(list_of_product_objects):
       input_yes_no_choice(message):
       input_press_to_continue(optional_message=''):
       input_new_product_and_price():

       changelog: (When,Who,What)
           RRoot,1.1.2030,Created Class
           AGibbs,6/6/2020,Modified code to complete assignment 8
       """
    pass

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
           Menu of Options
           1) Add a new Task
           2) Save Data to File        
           3) Reload Data from Saved File
           4) Exit Program
           ''')
        print()  # Add an extra line for looks


    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice


    @staticmethod
    def print_current_Products_in_list(list_of_product_objects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Prodict list contains: *******")
        print('Product Name   (Product Price)')
        for row in list_of_product_objects:
            print (row["Product"] + " (" + "$" + str(row["Price"]) + ")")
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
    def input_new_product_and_price():
        """ Gets user input for new task and priority

            :return: Product.product_name, Product.product_price
        """


        Product.product_name = input("Enter product name (text only): ")
        Product.product_price = float(input ('Enter price (number only): '))

        print('Product and Price added!')
        return Product.product_name, Product.product_price


# Presentation (Input/Output)  -------------------------------------------- #
# Main Body of Script  ---------------------------------------------------- #
# Step 1 - When the program starts, Load data from products.txt.
FileProcessor.read_data_from_file(strFileName, list_of_product_objects)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Products_in_list(list_of_product_objects)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(Product.product_name, Product.product_price, list_of_product_objects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.write_data_to_file(strFileName, list_of_product_objects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '3':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            FileProcessor.read_data_from_file(strFileName, list_of_product_objects)
            IO.print_current_Products_in_list(list_of_product_objects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
    else:
        print('Please select only from the menu of options')  # in case user makes a choice other than 1,2,3,4,
