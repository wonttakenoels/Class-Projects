# Class-Projects
url: api.openweathermap.org 
import requests
import json
#import pandas as pd
import time


def list_of_days(list_days):
    #This function prints out the Details for the day's expected forecast

     for item in list_days['daily']:

         print('Date: '+ str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['dt']))))
         print('Expected minimum temperature: '+str(item['temp']['min']))
         print('Expected maximum temperature: ' +str(item['temp']['max']))
         print('Expected Weather Description: '+str(item['weather'][0]['description']))
         print('\n')


def main():


    while True:
        user_location=input('Enter your Zip Code(e.g. 11112) or City Name(e.g. Berlin,DE): ')

        try:
             resp=requests.get('https://openweathermap.org/data/2.5/find?q='+str(user_location)+'&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric')
             #request.get is used to get the data from the get  call
             result=resp.json()
             #Convert response to json so its iterable
             while len(result['list'])==0:
                  print('invalid Zip Code or City Name entered')
                  user_location=input('Enter your Zip Code(e.g. 11112) or City Name(e.g. Berlin,DE): ')
                  resp=requests.get('https://openweathermap.org/data/2.5/find?q='+str(user_location)+'&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric')
                  result=resp.json()
             print('successful connection')
            # Show current day's temperature and weather description
             current_location=result['list'][0]['name']

             desc=result['list'][0]['weather'][0]['description']
             current_temp=result['list'][0]['main']['temp']
             feels_like=result['list'][0]['main']['feels_like']

             #Print current day's weather
             print('Current Location: '+str(current_location))
             print('Current Temp(in Celcius): '+str(-273.15+current_temp))
             print('feels like(in Celcius) '+str(-273.15+feels_like))
             print('Current Weather description:'+str(desc))

             #Get  lat/lon of current location which will be used to get 7 day forecast of given location
             coord=result['list'][0]['coord']

             resp2=requests.get('https://openweathermap.org/data/2.5/onecall?lat='+str(coord['lat'])+'&lon='+str(coord['lon'])+'&units=metric&appid=439d4b804bc8187953eb36d2a8c26a02')
             result2=resp2.json()
             print('\n')
             print('Weather Forecast over the next 8 days(including today): ')
             print('\n')

             list_of_days(result2)


        except:
                print('Unsuccessful connection')


main()
