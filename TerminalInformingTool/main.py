from menu import menu
import informations as info

main_menu=menu('Main',True,"Weather","Test2","Test3")

if main_menu==1:
    weather_data=info.get_weather_informations_continent("/europa/EU.html")
    #Load Weather loads the saved Weather data if there not over 30 minutes old, if there over 30 minutes old scrap the data based on the setting, from the website
    Weather_menu=menu('Weather',True,"Refresh Data","Setup Location","Load Weather")
    if Weather_menu==1:
        pass
        #if location_setup already done and save data locatet, scrap data from the website, based on the saved settings 
    elif Weather_menu==2:
        weather_location_data=info.get_weather_informations_continent("/europa/EU.html")
        info.setup_location(weather_location_data)
    elif Weather_menu==3:
        #add function that prints out the weather_data
        weather_data=menu("Weather Informations",False)#adding function that checks if a save file for the weather exists and if it does read data out of it and put it in the function, infront, as a paramter
      