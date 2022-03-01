from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def test_plot_water_levels(): 
    stations = build_station_list()
    dates, levels = fetch_measure_levels(stations[0].measure_id,dt=datetime.timedelta(days=10))
    plot_water_levels(stations[0], dates, levels)

def test_plot_water_levels_with_fit():
    stations = build_station_list()
    dates, levels = fetch_measure_levels(stations[0].measure_id,dt=datetime.timedelta(days=2))
    plot_water_level_with_fit(stations[0], dates, levels, 10)