from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from colorama import Fore, Back, Style


def run():
    stations = build_station_list()

    update_water_levels(stations)

    water_level_stations = stations_highest_rel_level(stations, 960)

    station_towns = []

    for station in water_level_stations:
        if station.town != None:
            details = (station.town, station.relative_water_level())
            station_towns.append(details)

    
    used_stations =[]
    low_risk = []   
    moderate_risk =[]
    high_risk = []
    severe_risk =[]
    for i in range(len(station_towns)):
        if station_towns[i][0] not in used_stations:
            used_stations.append(station_towns[i][0])
            if station_towns[i][1] <= 1:
                low_risk.append(station_towns[i][0])
            elif station_towns[i][1] > 1 and station_towns[i][1] <= 2 :
                moderate_risk.append(station_towns[i][0])
            elif station_towns[i][1] > 2 and station_towns[i][1] <= 4 :
                high_risk.append(station_towns[i][0])
            elif station_towns[i][1] >= 4 :
                severe_risk.append(station_towns[i][0])
            
    print(Fore.GREEN + "Low risk towns are: " + str(low_risk))
    print(Style.RESET_ALL)
    print(Fore.YELLOW + "Moderate risk towns are: " + str(moderate_risk))
    print(Style.RESET_ALL)
    print(Fore.LIGHTRED_EX +"High risk towns are: " + str(high_risk))
    print(Style.RESET_ALL)
    print(Back.RED + "Severe risk towns are: " + str(severe_risk))
    print(Style.RESET_ALL)
        





if __name__ == "__main__":
    print("* Task 2G: CUED Part IA Flood Warning System *")
    run()