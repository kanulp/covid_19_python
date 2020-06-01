import pandas as pd
import matplotlib.pyplot as plt
import geopandas

link = "https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv"
data = pd.read_csv(link)


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

ax = world[world.continent == 'Canada'].plot(
    color='white', edgecolor='black')

gdf = geopandas.GeoDataFrame(
    data, geometry=geopandas.points_from_xy(data['Reporting_PHU_Longitude'], data['Reporting_PHU_Latitude']))
gdf.plot(ax=ax, color='red')

plt.show()

