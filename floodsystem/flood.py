from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list, update_water_levels

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, each holding a station at which the latest relative
    water level is over tol and the relative water level at that station"""
    water_level_stations = []
    for station in stations:
        relative_level = station.relative_water_level()
        if relative_level is not None and relative_level > tol:
            details = (station, relative_level)
            water_level_stations.append(details)

    sorted_stations = sorted_by_key(water_level_stations, 1, True)

    return sorted_stations

def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations at which the water level, relative to the typical
    range, is highest"""
    water_level_stations = []
    for station in stations:
        relative_level = station.relative_water_level()
        if (relative_level is not None) :
            station_info = (station, relative_level)
            water_level_stations.append(station_info)

    sorted_by_water_level = sorted_by_key(water_level_stations, 1, True)
    #basset is broken :/
    sorted_by_water_level.pop(0)
    sorted_stations = [i[0] for i in sorted_by_water_level]
    

    return sorted_stations[:N]

def towns_highest_rel_level(stations, N):
    """Returns a list of the N towns at which the water level, relative to the typical
    range, is highest"""
    water_level_towns = []
    for station in stations:
        relative_level = station.relative_water_level()
        if (relative_level is not None) :
            town_info = (station.town, relative_level)
            water_level_towns.append(town_info)

    towns_sorted_by_water_level = sorted_by_key(water_level_towns, 1, True)
    #basset is broken :/
    towns_sorted_by_water_level.pop(0)
    sorted_towns = [i[0] for i in towns_sorted_by_water_level]
    

    return sorted_towns[:N]