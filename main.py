from menu import menu
import informations as info

main_menu=menu('Main',"Weather","Test2","Test3")

if main_menu==1:
    weather_data=info.get_weather_informations_continent("/europa/EU.html")
    Weather_menu=menu('Weather',"Refresh Data","Setup Location","Load Weather")
    if Weather_menu==1:
        pass
        #if statement looking if data exist 
    elif Weather_menu==2:
        weather_location_data=info.get_weather_informations_continent("/europa/EU.html")
        info.setup_location(weather_location_data)