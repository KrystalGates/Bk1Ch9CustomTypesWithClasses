import datetime
# In this exercise, you are going to define your own Building type and create several instances of it to design your own virtual city. Create a class named Building in the building.py file and define the following fields, properties, and methods.

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories

class Building:
    def __init__(self, address, stories):
        self.designer = "",
        self.date_constructed = ""
        self.owner = "",
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = f"{datetime.datetime.now():%m/%d/%y}"

    def purchase(self, owner):
        self.owner = owner

    def print_building_info(self):
        print(f'{self.address} was purchased by {self.owner} Builder on  {self.date_constructed} and has {self.stories} stories.')

# Methods
# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

# Constructor
# Define your __init__ method to accept two arguments
# address
# stories

# Once defined this way, you can send those values as parameters when you create each instance

# Creating Your Buildings
# Create 5 building instances
eight_hundred_eighth = Building("800 8th Street", 12)
eight_hundred_eighth.purchase("Bobby")
eight_hundred_eighth.construct()
eight_hundred_eighth.print_building_info()

fourty_fifth = Building("402 45th Street", 14)
fourty_fifth.purchase("Rover")
fourty_fifth.construct()
fourty_fifth.print_building_info()

broadway = Building("700 Broadway Street", 5)
broadway.purchase("Jacob")
broadway.construct()
broadway.print_building_info()

seasame = Building("123 Sesame Street", 36)
seasame.purchase("Big Bird")
seasame.construct()
seasame.print_building_info()

charlotte = Building("67 Charlotte Street", 9)
charlotte.purchase("Smalls")
charlotte.construct()
charlotte.print_building_info()
# Have each one get purchased by a real estate magnate
# After purchased, construct each one
# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.