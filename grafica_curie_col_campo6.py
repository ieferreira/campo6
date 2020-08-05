# Importar las librerias usadas 

import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import pandas as pd
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

# Datos Originales de Li et al, 2017

# Datos filtrados para mostrar Colombia
 # guardar como .csv para uso posterior

# Datos filtrados para la zona de campo



choice = input("¿Graficar para Colombia (col) o para la zona de campo 6 (6)? (col/6): \n")

while choice not in ["col", "6"]:
    print("la zona no se reconoce, deseas Colombia (col) o Campo 6 (6)")
    choice = input("¿Graficar para Colombia (col) o para la zona de campo 6 (6)? (col/6): \n")

if choice == "col":
    data2 = pd.read_csv("curie_colombia.csv")

    fig = plt.figure(figsize=(9,6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    plt.title('Zona ubicada en contexto Regional'.title())
    # ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    ax.set_extent([-80, -65, -1.8, 11], ccrs.PlateCarree())
    # ax.stock_img()
    scaled_c=(data2["CUR"].astype(float)-data2["CUR"].astype(float).min())/(data2["CUR"].astype(float).max()-data2["CUR"].astype(float).min())
    ax.coastlines(resolution='50m')

    img = plt.scatter(data2["LON"], data2["LAT"],s=100, marker='s', c=-data2["CUR"].astype(float), cmap=plt.cm.rainbow)
    plt.scatter(-74,4, marker='*', s=100, color='black',label="Zona Campo 6")
    clb = plt.colorbar(img, shrink=0.5, aspect=15)
    clb.set_label("Profundidad a Punto de CUrie (Km)")
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                    linewidth=2, color='gray', alpha=0.5, linestyle='--')

    plt.scatter(-72.5,8, marker='s', s=50, color='white',label="Dato No Disponible")
    gl.xlabels_top = False
    gl.ylabels_left = True
    gl.ylabels_right = False
    gl.xlines = True
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}

    plt.legend()
    plt.show()
elif choice == "6":
    data3 = pd.read_csv("curie_zona_campo.csv")
    fig = plt.figure(figsize=(9,5))
    ax = plt.axes(projection=ccrs.PlateCarree())
    plt.title('Zona Campo 6 - Grupo Río Guayuriba - Río Negro')
    ax.set_extent([-74.45, -73.4, 3.4, 4.4], ccrs.PlateCarree())
    img2 = plt.scatter(data3["LON"], data3["LAT"],s=2000, marker='s', c=-(data3["CUR"].astype(float)), cmap=plt.cm.rainbow)
    clb = plt.colorbar(img2, shrink=0.5, aspect=15)
    clb.set_label("Profundidad a Punto de CUrie (Km)")
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                    linewidth=2, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_left = True
    gl.ylabels_right = False
    gl.xlines = True
    gl.xlocator = mticker.FixedLocator([-74.6,-74.4,-74.2, -74.0, -73.8, -73.6,-73.4])
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 10, 'color': 'black'}
    gl.ylabel_style = {'size': 10, 'color': 'black'}
    plt.show()