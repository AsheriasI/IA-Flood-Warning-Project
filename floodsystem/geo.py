# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from math import radians, cos, sin, asin, sqrt
from .utils import sorted_by_key  # noqa

def haversine(func_coordinate, func_p):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """

    lon1, lat1 = func_coordinate[0], func_coordinate[1]
    lon2, lat2 = func_p[0], func_p[1]
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r



def stations_by_distance(stations,p):
    """Given a list of station objects and a coordinate, the function returns a list of tuples
    (station, distance)"""
    distances = []
    for station in stations:
        coordinate = station.coord
    
    # Apply haversine to find distances and attribute to tuple list
        distance = haversine(coordinate, p)
        distances.append((station, distance))
    
    # Sort list by distances
    sorted_distances = sorted_by_key(distances,1)

    return sorted_distances

def stations_within_radius(stations, centre, r):
    stations_in_radius = []
    for station in stations:
        # Find distances from defined centre
        distance = haversine(station.coord, centre)
        # Define validity of difference and if to add to list
        if distance <= r:
            stations_in_radius.append(station)

    return stations_in_radius

def stations_by_river(stations):
    """Returns a dictionary containing rivers (keys), and the stations on each river (values)"""
    rivers = {}
    for station in stations:
        # only add the river if station.river has been set
        river = station.river
        if river is not None:
            # add the station to the river key in the dictionary
            # if the key is not in the dictionary, add it
            if river in rivers:
                rivers[river].append(station)
            else:
                rivers[river] = [station]

    return rivers
    
def rivers_with_station(stations):
    """Returns the names of rivers on which a station is situated"""
    return set(stations_by_river(stations).keys())

def rivers_by_station_number(stations, N):
    # Returns a list of tuples (river, number of stations on that river)
    river_counts = []
    river_dict = stations_by_river(stations)
    for (river, river_stations) in river_dict.items():
        river_counts.append((river, len(river_stations)))

    # sort the list of rivers by number of stations, from highest to lowest
    sorted_rivers = sorted_by_key(river_counts, 1, reverse=True)

    sorted_river_subset = []
    # Adds the highest value rivers to list until N
    for i in range(N):
        sorted_river_subset.append(sorted_rivers[i])
    tie_cond = False
    # Adds any rivers with equal value to Nth term to the list
    while not tie_cond:
        if sorted_rivers[len(sorted_river_subset)-1] == sorted_rivers[len(sorted_river_subset)]:
            sorted_river_subset.append(sorted_rivers[len(sorted_river_subset)])
        else:
            tie_cond = True

    return sorted_river_subset