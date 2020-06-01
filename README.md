# covid_19_python

## Ploting and analyzing covid-19 ontario data.

## Output
![alt text](https://raw.githubusercontent.com/kanulp/covid_19_python/master/chart.png)


## Code 
```python 

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

```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some libraries.

```bash
pip install pandas
pip install geopandas
```
Run Python Covid.py 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) [2020] [Karan Gajjar]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
