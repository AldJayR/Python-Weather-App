import pytest
from unittest.mock import patch
from project import get_weather, get_random_city, display_weather_data, get_country_and_city

def test_get_random_city():
    city = get_random_city()
    assert city in [
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

@patch('builtins.input', side_effect=["Test Country", "Test City"])
def test_get_country_and_city(mock_input):
    city, country = get_country_and_city()
    assert city == "Test City"
    assert country == "TEST COUNTRY"


