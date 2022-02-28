# Find reative level of every station
# Add risk assesment to each Relative level
# For every station with a risk assesment, add the respective town to the list of that risk assesment
# Starting from 'Severe' remove all towns in severe from L M H, etc, til each town is only in one lsit
# Print each list



from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level, towns_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

stations = build_station_list()
update_water_levels(stations)
at_risk_towns = towns_highest_rel_level(stations, N)
print(at_risk_towns)