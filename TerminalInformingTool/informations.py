import requests
from bs4 import BeautifulSoup
import lxml
from TerminalInformingTool.menu import menu
import os
import pandas as pd

def for_item_in_updater(data,dictionary):
    for items in data:
        dictionary.update({items.text : items.get("value")})


def get_weather_informations_continent(sublink):
    mainlink="https://www.wetter.com"
    website=requests.get(mainlink+sublink).text
    soup=BeautifulSoup(website,"lxml")
    #get the informations for the sublink
    continents=soup.find('select', attrs={"aria-label":"Kontinent auswählen"}).find_all("option")
    #returns a dictionary with all the available continents
    continents_saved={}
    for_item_in_updater(continents,continents_saved)
    print(continents_saved)
    return continents_saved

def get_weather_informations_country(sublink):
    mainlink="https://www.wetter.com"
    website=requests.get(mainlink+sublink).text
    soup=BeautifulSoup(website,"lxml")
    #get the informations for the sublink
    country=soup.find('select', attrs={"aria-label":"Land auswählen"}).find_all("option")
    #returns a dictionary with all the available countrys
    country_saved={}
    for_item_in_updater(country,country_saved)
    return country_saved

def get_weather_informations_city(sublink):
    mainlink="https://www.wetter.com"
    website=requests.get(mainlink+sublink).text
    soup=BeautifulSoup(website,"lxml")
    #get the informations for the sublink
    city=soup.find('select', attrs={"aria-label":"Stadt auswählen"}).find_all("option")
     #returns a dictionary with all the available citys
    city_saved={}
    for_item_in_updater(city,city_saved)
    return city_saved

def get_weather_informations_time(sublink):
    mainlink="https://www.wetter.com"
    website=requests.get(mainlink+sublink).text
    soup=BeautifulSoup(website,"lxml")
    #get the informations for the sublink
    temperature=soup.find(class_="delta rtw_temp").text
    weather_type=soup.find(class_="text--small rtw_weather_txt mb--").text
    location=soup.find(class_="delta text--white mb--").text

     #scraps the data about the time and temparatur
    time_saved={}
    time_saved.update({"location":location})
    time_saved.update({"temperature":temperature})
    time_saved.update({"Weather Type":weather_type})
    #returns a dictionary with all the available times
    return time_saved

def sava_data(file_location,filename,data):
    if os.name('nt'):
        full_path=file_location+"\\"+filename
    else:
        full_path=file_location+"/"+filename
    if os.path.exists(full_path):
        #add functionallity later
        data=pd.read_csv(full_path)
    else:
        file=open(full_path,'w')
        file.write(data)
        file.close




def setup_location(continents_saved):
    continents=menu("select Continent",*continents_saved.keys())
    #if this for function work use the keys_to_list function
    continents_keys_for_index=list(continents_saved.keys())
    continent_index = continents - 1
    continent_key = continents_keys_for_index[continent_index]
    continent_sublink = continents_saved[continent_key]
    
    country_data=get_weather_informations_country(continent_sublink)
    countries=menu("select country",*country_data.keys())
    country_keys_for_index=list(country_data.keys())
    country_index = countries - 1
    country_key = country_keys_for_index[country_index]
    country_sublink = country_data[country_key]
    
    city_data=get_weather_informations_city(country_sublink)
    citys=menu("select City",*city_data.keys())
    city_keys_for_index=list(city_data.keys())
    city_index = citys - 1
    city_key = city_keys_for_index[city_index]
    city_sublink = city_data[city_key]

    time_data=get_weather_informations_time(city_sublink)
    times=menu("select the Time you want the Data for",*time_data.keys())
    time_keys_for_index=list(time_data.keys())
    time_index = times - 1
    time_key = time_keys_for_index[time_index]
    time_sublink = time_data[time_key]