# -*- coding: utf-8 -*-
import pandas as pd
import shapefile
import geopandas as gpd
import matplotlib.pyplot as plt

def color_plot(shape_file_path, data_file_path, plot_column):
    sf = shapefile.Reader(shape_file_path, encoding='SHIFT-JIS').__geo_interface__
    df = gpd.GeoDataFrame.from_features(sf)

    data = pd.read_excel(data_file_path, encoding='utf-8', header=1, index_col=0)

    show_data = pd.merge(df, data, left_on='KIGO_I', right_on='町丁目名', how='left')

    show_data.plot(
        column=plot_column,
        figsize=[5,5],
        cmap="Oranges",
        missing_kwds={'color': 'lightgrey'}
    )
    plt.show()
