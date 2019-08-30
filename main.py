# Open the main.py file and import the Building class from building.py. Once you have defined your City class, also import that into main.py. For this exercise, all the logic of constructing buildings and building your city will be in city.py, so take all of your logic from building.py and move it over.

from building import Building, eight_hundred_eighth, fourty_fifth, broadway, seasame, charlotte
from city import City

# Create a new city instance and add your buildings to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

megalopolis = City()
# print(eight_hundred_eighth)


megalopolis.add_multi_buildings([eight_hundred_eighth,fourty_fifth, broadway, seasame, charlotte])

# Awesome code here

for building in megalopolis.city_buildings:
    print(building)