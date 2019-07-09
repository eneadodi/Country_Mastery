import os, sys

#'/home/user/example/parent/child'
current_path = os.path.abspath('.')

#'/home/user/example/parent'
parent_path = os.path.dirname(current_path)

sys.path.append(parent_path)

from bs4 import BeautifulSoup, SoupStrainer, Tag
from PIL import Image
import sys
import requests
import lxml
import Geographical_Information as gi
import urllib3
import urllib.request

class Country_Information_Scrapper(object):

    """
    Constructor
    """
    def __init__(self):
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    """
    param: url
    return the Entire HTML code fo the website
    """
    def getEntireHTMLPage(self,url):
        page = requests.get(url,headers=self.HEADERS).text
        soup = BeautifulSoup(page,features ="lxml")
        return soup

    def extract_all_country_information_from_continent(self,continent):
        continent = continent.name.lower()
        url = "http://flagpedia.net/continent/" + continent
        soup = self.getEntireHTMLPage(url)

        """strains it to just the main content"""
        country_section = soup.find("section",{"id":"countries"})
        all_countries = country_section.find_all("article")
        #print(all_countries)

        """For every country article, we have to get name,image of flag, area,
        capital city, population size, and flag
        the geographical location will be scrapped from another website!"""
        for c in all_countries:
            name_header = c.find("h2")
            name_of_country = name_header.text

            cap_pop_area = c.find("aside").find("dl").find_all("dd")

            image_div = c.find("div")
            image_url = "https:" + image_div.find("img")['src']

            """This section gets the image of the flags from flagpedia.net! Shout outttt"""
            flag_file_name = name_of_country + "-flag"
            with open(flag_file_name,'wb') as f:
                f.write(urllib.request.urlopen(image_url).read())
                image_flag = Image.open(flag_file_name)

            """Automatically adds path to the geology.com website. Shout out to geology.com!"""
            geographical_location_image_url_specifier = name_of_country.lower().replace(" ", "-").replace("the","") + ".gif"
            geographical_location_image_url = "https://geology.com/world/map/map-of-"+geographical_location_image_url_specifier
            if name_of_country == "Cote d'Ivoire":
                geographical_location_image_url = "https://geology.com/world/map/map-of-"+"ivory-coast.gif"

            location_file_name = name_of_country + "-location"
            with open(location_file_name,'wb') as f:
                f.write(urllib.request.urlopen(image_url).read())
                image_location = Image.open(location_file_name)

            country = gi.Country(name_of_country,image_flag,image_location,cap_pop_area[0].text,cap_pop_area[1].text,
            cap_pop_area[2].text)
            print(name_of_country = "Finished!\n")




cis = Country_Information_Scrapper()
Africa = gi.Continent("Africa")
cis.extract_all_country_information_from_continent(Africa)
