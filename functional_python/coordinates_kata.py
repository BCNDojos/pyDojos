import csv
import itertools
from haversine import haversine


def is_europe(row):
    continent = row[5]
    return continent == 'Europe'


def pick_lat_lon(city_tuple):
    lat = float(city_tuple[2])
    lon = float(city_tuple[3])
    return lat, lon


def get_distance(two_cities_tuple):
    coordinates = map(pick_lat_lon, two_cities_tuple)
    return haversine(*coordinates)


with open('country-capitals.csv') as csv_file:
    capitals_iterator = csv.reader(csv_file)
    european_capitals = filter(is_europe, capitals_iterator)
    city_pairs = itertools.combinations(european_capitals, 2)
    remotest_cities = max(city_pairs, key=get_distance)

    print(get_distance(remotest_cities))
