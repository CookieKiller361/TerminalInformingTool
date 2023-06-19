from menu import menu
import Weather_informations as info
import file_handeling as fh

main_menu=menu('Main',True,"Weather","Test2","Test3")

if main_menu==1:
    weather_data=info.get_weather_informations_continent("/europa/EU.html")
    Weather_menu=menu('Weather',True,"Load Weather","Setup Location")
    if Weather_menu==1:
        #add function that prints out the weather_data
        weather_data_now=info.load_weather("TerminalinformingTool/setting_saved.csv","setup_weather")
        if weather_data_now != False:
            weather_data_now=info.get_weather_informations_time(weather_data_now)
            weather_data=menu("Weather Informations",False,weather_data_now)
        else: 
            weather_data_now='please make the setup for the location befor you try to load the data!'
            weather_data_now=fh.convert_to_dictionary("error",weather_data_now)   
            weather_data=menu("Weather Informations",False,weather_data_now)
    elif Weather_menu==2:
        weather_location_data=info.get_weather_informations_continent("/europa/EU.html")
        info.setup_location(weather_location_data)