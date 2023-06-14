import requests
from bs4 import BeautifulSoup
import lxml

def get_weahter_informations():
    website=requests.get("https://www.wetter.com/europa/EU.html").text
    soup=BeautifulSoup(website,"lxml")
    #get the informations for the sublink
    continents=soup.find('select', attrs={"aria-label":"Kontinent auswählen"}).find_all("option")
    country=soup.find('select', attrs={"aria-label":"Land auswählen"}).find_all("option")
    city=soup.find('select', attrs={"aria-label":"Kontinent auswählen"}).find_all("option")
    time=soup.find('select', attrs={"aria-label":"Zeitraum auswählen"}).find_all("option")

    #returns a dictionary with all the available continents
    continents_saved={}
    for continent in continents:
        continents_saved.update({continent.text : continent.get("value")})
    
    #returns a dictionary with all the available countrys
    country_saved={}
    for countrys in country:
        country_saved.update({countrys.text : countrys.get("value")})

    #returns a dictionary with all the available citys
    city_saved={}
    for citys in city:
        city_saved.update({citys.text : citys.get("value")})

    #returns a dictionary with all the available times
    time_saved={}
    for times in time:
        time_saved.update({times.text : times.get("value")})


    return continents_saved, country_saved, city_saved, time_saved