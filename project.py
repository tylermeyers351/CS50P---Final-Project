"""
    City Population & Weather Program
    Author: Tyler Meyers
    
    API URL: https://openweathermap.org/
    Original CSV: https://simplemaps.com/data/world-cities

"""

import requests
import csv
import json


def main():
    api_key = 'bcfc2df24a378133f58290e10a59a5e0'
    user_city = input("Enter City: ").strip().title()

    city, country, population = get_city_data(user_city)
    print("\n------------------------------")
    print(f"{city}, {country}")
    print(f"Population: {population}")

    temperature, weather = get_weather(user_city, api_key)
    print(f'Temperature: {temperature}°F')
    print(f'Weather: {weather}')

    emoji = get_emoji(temperature)
    print(emoji)
    print("------------------------------\n")


def get_city_data(user_city):
    cities = []

    with open("worldcities.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cities.append({"city": row["city"], "country": row["country"], "population": row["population"]})
    for city in cities:
        if user_city == city["city"]:
            population = int(city['population'])
            population_with_commas = "{:,}".format(population)

            return city['city'], city['country'], population_with_commas
    raise ValueError("Please enter valid city")


def get_weather(user_city, api_key):
    # Send an API request to the weather service, return temperature and weather
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}')
    data = response.json()

    # print(json.dumps(data, indent=2)) --> dumps all data available
    temperature = int(((data['main']['temp']) - 273.15) * 9/5 + 32)

    weather = data['weather'][0]['description']
    weather_formatted = weather.title()

    return temperature, weather_formatted


def get_emoji(temperature):
    # Function takes temperature (in Farenheit) and outputs an emoji reaction
    if temperature < 32:
        return '🥶🥶🥶'
    elif temperature < 52:
        return '😁😁😁'
    elif temperature < 72:
        return '😛😛😛'
    elif temperature < 92:
        return '😅😅😅'
    else:
        return '🥵🥵🥵'


if __name__ == "__main__":
    main()