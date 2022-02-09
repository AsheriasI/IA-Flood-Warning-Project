# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from math import radians, cos, sin, asin, sqrt

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

from .utils import sorted_by_key  # noqa

def stations_by_distance(stations,p):
    """Given a list of station objects and a coordinate, the function returns a list of tuples
    (station, distance)"""
    distances = []
    for station in stations:
        coordinate = station.coord
        distance = haversine(coordinate, p)
        distances.append((station, distance))

    sorted_distances = sorted_by_key(distances,1)

    return sorted_distances

def stations_within_radius(stations, centre, r):
    stations_in_radius = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
            stations_in_radius.append(station)

    return stations_in_radius