import requests  #imports needed modules
import sys

def start():  # defines start function
    user_selection = input("\nPress 1 to search by zip code or 2 to search by city name: ")  #recieves input from user to search by zip or city name

    if user_selection == str(1):  # statement that runs the users selection
        selection1()
    elif user_selection == str(2):
        selection2()
    else:                         # shows user that they made an invalid selection and restarts the program so they can try again.
        print("ERROR: Invalid Selection")
        restart()

    restart()  #runs restart function after initial use if user would like to make another input


def restart():  # defines restart function so that it can be used where needed
    restart = input("\nPress Y to restart or any other button to exit: ").lower()  #accepts user input if they would like to restart
    if restart == 'y':
        start()
    else:
        print("\nGoodbye\n")  #prints goodbye message and closes application is user does not select y
        sys.exit()


def selection1():  # defines function that allows user to search by zip
    zip_code = input("Please enter Zip Code: ")  #sets zip code variable

    # sets variable that gets information from API by zip
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units=imperial&appid=e8d2ba9706d1d0532b51670a8f124e05")
    
    weather = response.json()   # converts response variable to json

    try:  #exception handling to ensure data is recieved, if not likely due to invalid input
        wx_data(weather)
    except:  #prints error and restarts the application
        print("ERROR: Zip code is not valid.")   
        restart() 

    
def selection2(): # defines function that allows user to search by name
    city_name = input("Please enter city name: ")        

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid=e8d2ba9706d1d0532b51670a8f124e05")

    weather = response.json()
    
    try:
        wx_data(weather)
    except:
        print("ERROR: City name is not valid.")   
        restart() 


def wx_data(weather):  # sets function to recieve weather information that uses weather as an argument
    location = weather['name']  # variables with information requested from API
    temp = weather['main']['temp']
    feel = weather['main']['feels_like']
    hightemp = weather['main']['temp_max']
    lowtemp = weather['main']['temp_min']
    wind_speed = weather['wind']['speed']
    clouds = weather['clouds']['all']
    pressure = weather['main']['pressure']
    latitude = weather['coord']['lat']
    longitude = weather['coord']['lon']
    humidity = weather['main']['humidity']
    description = weather['weather'][0]['description']

    print(f'\nThe current forecast for {location} is:')  # displays weather information to user
    print(f'Current Temperature : {temp} Degrees Fahrenheit')
    print(f'Temperature Feels Like : {feel} Degrees Fahrenheit')
    print(f'High Temperature : {hightemp} Degrees Fahrenheit')
    print(f'Low Temperature : {lowtemp} Degrees Fahrenheit')
    print(f'Wind Speed : {wind_speed} Mph')
    
    if clouds >= 7:    # if statement used to display a description for cloudiness
        print('Clouds : Mostly Cloudy')
    elif clouds >= 3:
        print('Clouds : Partly Cloudy')
    else:
        print('Clouds : Few to none.')    

    print(f'Pressure : {pressure} hPa')
    print(f'Latitude : {latitude}')
    print(f'Longitude : {longitude}')
    print(f'Humidity : {humidity}%')
    print(f'Description : {description.title()}')
    




print("\nWelcome to my forecast tool!")   # prints initial welcome message

start() # method call to start the application

