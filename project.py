import requests
import random
from tabulate import tabulate
from pyfiglet import Figlet
import csv
import sys
import time
import os

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')


f = Figlet(font='slant')


def main():
    display_screen()
    get_input()


def display_screen():
    try:
        with open('menu.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        print(f.renderText("PYTHON WEATHER APP"))
        print(tabulate(data, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found.")


def get_weather(city, country=None):
    if country:
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={WEATHER_API_KEY}&units=metric"
    else:
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(base_url)
    return response.json()


def get_random_city():
    cities = [
        "Tokyo", "New York", "London", "Paris", "Berlin", "Los Angeles", "Sydney",
        "Beijing", "Moscow", "Rio de Janeiro", "Mumbai", "Cairo", "Madrid", "Toronto",
        "Bangkok", "Dubai", "Singapore", "Rome", "Istanbul", "Mexico City", "Johannesburg",
        "Seoul", "Buenos Aires", "Melbourne", "Athens", "São Paulo", "Vancouver", "Amsterdam",
        "Zurich", "Hong Kong", "Lisbon", "Barcelona", "Oslo", "Stockholm", "Kuala Lumpur",
        "Jakarta", "Delhi", "Warsaw", "Vienna", "Prague", "Brussels", "Budapest", "Havana",
        "Cape Town", "Dublin", "Karachi", "Lima", "Manila", "Kathmandu",
        "Oslo", "Reykjavik", "Helsinki", "Edinburgh", "Copenhagen", "Santiago", "Bogota",
        "Abuja", "Nairobi", "Auckland", "Perth", "Geneva", "Frankfurt", "Hamburg", "Munich",
        "Lyon", "Toulouse", "Marseille", "Valencia", "Granada", "Seville", "Porto",
        "Lagos", "Casablanca", "Rabat", "Tangier", "Addis Ababa", "Algiers", "Dakar"
    ]

    return random.choice(cities)


def display_weather_data(weather_data):
    if weather_data["cod"] != "404":
        main = weather_data.get("main", {})
        weather_description = weather_data.get("weather", [{}])[0].get("description", "No data available").capitalize()
        temperature = main.get("temp", "N/A")
        real_temp = main.get("feels_like", "N/A")
        temp_min = main.get("temp_min", "N/A")
        temp_max = main.get("temp_max", "N/A")

        print("\nWeather for", weather_data.get("name", "Unknown location"))
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {real_temp}°C")
        print(f"Min: {temp_min}°C")
        print(f"Max: {temp_max}°C")
        print(f"Weather for today: {weather_description}")
    else:
        print("City Not Found!")


def get_multiple_cities_weather():
    try:
        city_list = input("Enter multiple cities. Separate them with commas: ").split(", ")
    except EOFError:
        print()
        return

    for city in city_list:
        city = city.strip()
        display_weather_data(get_weather(city))


def get_input():
    while True:
        try:
            user_choice = int(input("Choose a number: "))
            break
        except ValueError:
            pass

    match user_choice:
        case 1:
            city, country = get_country_and_city()
            display_weather_data(get_weather(city, country))
        case 2:
            random_city = get_random_city()
            data = get_weather(random_city)
            display_weather_data(data)
        case 3:
            get_multiple_cities_weather()
        case 4:
            print("Exiting...")
            time.sleep(5)
            sys.exit()

        case _:
            print("Invalid choice.")


def get_country_and_city():
    while True:
        try:
            country = input("What's your country? ").strip().upper()
            city = input("What's your city? ").strip().title()

            if not city or not country:
                raise ValueError
            break
        except ValueError:
            pass
    return [city, country]


if __name__ == "__main__":
    main()
