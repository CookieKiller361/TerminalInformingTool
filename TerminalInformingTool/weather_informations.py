import requests
from bs4 import BeautifulSoup
import lxml
from menu import menu
import file_handeling as fh



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
    time_saved.update({"Location":location})
    time_saved.update({"Temperature":temperature})
    time_saved.update({"Weather Type":weather_type})
    #returns a dictionary with all the available times
    return time_saved

def setup_location(continents_saved):
    #setup for the Continents data
    continents=menu("select Continent",True,*continents_saved.keys())
    continents_keys_for_index=list(continents_saved.keys())
    continent_index = continents - 1
    continent_key = continents_keys_for_index[continent_index]
    continent_sublink = continents_saved[continent_key]
    #setup for the country data
    country_data=get_weather_informations_country(continent_sublink)
    countries=menu("select country",True,*country_data.keys())
    country_keys_for_index=list(country_data.keys())
    country_index = countries - 1
    country_key = country_keys_for_index[country_index]
    country_sublink = country_data[country_key]
    #setup for the city data
    city_data=get_weather_informations_city(country_sublink)
    citys=menu("select City",True,*city_data.keys())
    city_keys_for_index=list(city_data.keys())
    city_index = citys - 1
    city_key = city_keys_for_index[city_index]
    city_sublink = city_data[city_key]
    #setup for the time data
    time_data=get_weather_informations_time(city_sublink)
    #check if in progress if that makes sense, cause i changed the 
    # data from selecting time point to some importent informations
    times=menu("Weather data",False,time_data)
    
    #dont return this save it in the settings_data file
    
    data_finished_setup=fh.convert_to_dictionary("setup_weather",city_sublink)

    fh.add_data_with_checks("/TerminalinformingTool/","setting_saved.csv",'data_from',data_finished_setup)

def load_weather(filepath_for_csv_file,data_from_name):
    if_exist=fh.check_if_exist(filepath_for_csv_file)
    if if_exist==True:
        if_exist_in_file=fh.if_in_csv(filepath_for_csv_file,"data_from",data_from_name)
        if if_exist_in_file:
            return fh.search_saved_data(filepath_for_csv_file,"data_from",data_from_name)
        else:
            return "\ndata_item not in csv file"
    elif if_exist==False:
        return False