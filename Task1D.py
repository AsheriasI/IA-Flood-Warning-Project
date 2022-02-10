from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    #checking values with reference values
    print("Number of rivers: {}".format(len(rivers)))
    print("First ten rivers: {}".format(sorted(rivers)[:10]))

    #creating the dictionary
    rivers_dict = stations_by_river(stations)
    test_rivers = ("River Aire", "River Cam", "River Thames")
    
    #iterates through each test river's data to find stations on that river
    for river in test_rivers:
        stations_on_river = rivers_dict.get(river)
        #print(len(rivers_dict))
        station_names = [stat.name for stat in stations_on_river]
        print("Stations on {}: {}".format(river, station_names))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()