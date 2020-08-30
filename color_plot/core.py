# -*- coding: utf-8 -*-
import pandas as pd
import shapefile
import geopandas as gpd
import matplotlib.pyplot as plt
import os.path


def color_mapping(shape_file_path, data_file_path, plot_column):
    sf = shapefile.Reader(shape_file_path, encoding='SHIFT-JIS').__geo_interface__
    df = gpd.GeoDataFrame.from_features(sf)

    root, ext = os.path.splitext(data_file_path)
    if ext == '.xlsx':
        data = pd.read_excel(data_file_path, encoding='utf-8', header=0, index_col=0)
        print(data.head())
    elif ext == '.csv':
        data = pd.read_csv(data_file_path, encoding='utf-8')
    else:
        print('invalid file type')
        exit()
    

    show_data = pd.merge(df, data, left_on='KIGO_I', right_on='町丁目名', how='left')

    show_data.plot(
        column=plot_column,
        figsize=[5,5],
        cmap="Oranges",
        missing_kwds={'color': 'lightgrey'}
    )
    plt.show()

