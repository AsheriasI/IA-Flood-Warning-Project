# Find reative level of every station
# Add risk assesment to each Relative level
# For every station with a risk assesment, add the respective town to the list of that risk assesment
# Starting from 'Severe' remove all towns in severe from L M H, etc, til each town is only in one lsit
# Print each list



from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
for station in stations:
	print("station is " + station.name)
	print("town is " + station.town)