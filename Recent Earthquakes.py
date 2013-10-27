# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Use [urllib](http://docs.python.org/2/library/urllib.html) to open arbitrary resources by URL and pass that data to the [read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.io.parsers.read_csv.html) function of pandas. Then print out the first few rows of data using pandas [Indexing and Selecting Data](http://pandas.pydata.org/pandas-docs/dev/indexing.html).

# <codecell>

import urllib
from pandas import read_csv


url = 'http://earthquake.usgs.gov/earthquakes/catalogs/eqs7day-M1.txt'
data = read_csv(urllib.urlopen(url))

data[0:10]

# <markdowncell>

# **UH OH!** Note that our data is a bit *dirty* and contains a notice that this data feed has been deprecated:

# <codecell>

print data[0:1]['Src'].values[0]

# <markdowncell>

# We can filter out the dirty data using [dropna](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.dropna.html) to drop any rows that contain **NaN**.

# <codecell>

clean_data = data.dropna(axis=0, how='any')
clean_data[0:3]

# <markdowncell>

# In the code above note that I saved the results of `data.dropna()` into a different variable `clean_data` rather than over-writing the old variable `data`. **Why?** Why not just re-use old variable names? And if we did re-use old variable names what extra danger do we have to keep in mind while using the IPython Notebook?

# <markdowncell>

# Now let's just focus on earthquakes in Alaska (my home state! :)

# <codecell>

alaska = clean_data[clean_data.Src == 'ak']
alaska[0:10]

# <codecell>

from mpl_toolkits.basemap import Basemap
from matplotlib.cm import get_cmap

def plot_quakes(quakes, cmap, size):
    m = Basemap(llcrnrlon=-180,llcrnrlat=50.,
                urcrnrlon=-120.,urcrnrlat=72,
                resolution='l',area_thresh=1000.,projection='merc',
                lat_0=62.9540,lon_0=-149.2697)
    x, y = m(quakes.Lon, quakes.Lat)
    colors = arange(len(x))

    m.scatter(x, y, s=size, marker='o', c=quakes.Depth,
              cmap=cmap, alpha=0.7, zorder=10)

    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='coral',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    colorbar()
    return m

mycmap = get_cmap('Reds')
plot_quakes(alaska, mycmap, 100)

