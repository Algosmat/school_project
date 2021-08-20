
import shapefile
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np
from itertools import chain
#from shapely.geometry import Point


shape = shapefile.Reader("london.shp")

#First feature of the shapefile
feature = shape.shapeRecords()[0]
total_items = 0
for n in shape.shapeRecords():
    total_items += 1
features = [shape.shapeRecords()[n].shape.__geo_interface__ for n in range(total_items)]
first = feature.shape.__geo_interface__

#print(pd.DataFrame(first))

cordinate_item = [features[n]['coordinates'] for n in range(len(features)-1)]


clean_data = []

def flatten_by_recursion(multi_list):
    for data in multi_list:
        if type(data)==tuple:
            clean_data.append(data)
        else:
            flatten_by_recursion(data)

flatten_by_recursion(cordinate_item)
longitudes = [y for (x,y) in clean_data]
latitudes = [x for (x,y) in clean_data]

plt.plot(latitudes,longitudes)
plt.annotate('Barking',(548030,183363))
plt.annotate('Bloomsbury',(530123,182014))
plt.show()


