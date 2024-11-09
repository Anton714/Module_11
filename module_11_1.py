import requests
import numpy as np
import pandas as pd

print('_______ПОГОДА________')

API_T = '1daa1f8675c6270905502a5bc84921c7'
city = 'Snezhinsk'

params = {'q': city, 'APPID': API_T, 'units': 'metric'}

response = requests.get('https://pro.openweathermap.org/data/2.5/weather', params=params)

if response:
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)

    u_json = response.json()
    temp = u_json.get('main')

    print(f'Погода сейчас в {city} : \n'
          f'температура: {temp["temp"]} градусов Цельсия \n'
          f'ощущается: {temp["feels_like"]} градусов Цельсия\n'
          f'влажность: {temp["humidity"]} процентов')
    print()

    bs = pd.Series(u_json)

    print(bs)

    print()

    print(bs[['name', 'coord', 'wind']])
else:
    print()
    print('НЕТ ОТВЕТА ОТ СЕРВЕРА')
print()

print('________Data_Frame_______')
data = {'name': ['Rimma', 'Jon', 'Nik', 'Max', 'Lilu'],
        'age': [24, 41, 31, 19, 25],
        'country': ['Italy', 'India', 'Poland', 'Russia', 'Canada'],
        'level': [3, 5, 2, 7, 6]}
df = pd.DataFrame(data)
print(df)
