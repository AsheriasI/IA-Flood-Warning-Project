from numpy import floor_divide
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood 


def test_station_level_over_threshold():
    stations = build_station_list()
    flood.stations_level_over_threshold(stations, 0.8)

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    flood.stations_highest_rel_level(stations, 10)

def test_towns_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    flood.towns_highest_rel_level(stations, 10)