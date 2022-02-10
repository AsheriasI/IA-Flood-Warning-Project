#testing for geo functions

from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river, stations_within_radius
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    stations = build_station_list()
    distances = stations_by_distance(stations, (0,0))
    assert type(distances[0][1]) == float

#test_stations_by_distance()

def test_stations_within_radius():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    assert len(stations_within_radius(stations,p,1000 )) > 1

#test_stations_within_radius()