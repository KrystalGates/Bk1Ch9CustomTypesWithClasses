# In the previous Urban Planner exercise, you practices defining custom types to represent buildings. Now you need to create a type to represent your city. Here are the requirements for the class. You define the properties and methods.

# 1. Name of the city.
# 2. The mayor of the city.
# 3. Year the city was established.
# 4. A collection of all of the buildings in the city.
# 5. A method to add a building to the city.

# Remember, each class should be in its own file. Define the City class in the city.py file.

class City:
    def __init__(self):
        self.city = "",
        self.city_mayor = "",
        self.year_established = None,
        self.city_buildings = []

    def add_multi_buildings(self, building):
        self.city_buildings.extend(building)

    def add_building(self, building):
        self.city_buildings.append(building)
