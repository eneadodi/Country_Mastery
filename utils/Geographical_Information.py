
from PIL import Image


class Country(object):

    def __init__(self,name,geographical_location,flag_image,capital_city="Shinshigonshima",population_size=2000,total_area = "900,000"):
        self.name = name
        self.total_area = total_area
        self.capital_city = capital_city
        self.population_size = population_size
        self.geographical_location = geographical_location
        self.flag_image = flag_image

class Continent(object):

    def __init__(self,name):
        self.name = name
        countries = []

class Earth(object):

    def __init__(self):
        self.continents = {"Europe":Continent("Europe"),"Africa":Continent("Africa"),"Asia":Continent("Asia")
        ,"Antartica":Continent("Antartica"),"Oceania":Continent("Oceania")
        ,"North America":Continent("North America"),"South America":Continent("South America")}
