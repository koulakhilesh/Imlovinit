#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:27:40 2021

@author: akhilesh.koul
"""

import numpy as np
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from tqdm import tqdm
from shapely.geometry import Point
from shapely.ops import cascaded_union
from shapely.ops import unary_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords


class imlovint():
    
    def __init__(self,chain='mcd',sg_region_shape=None):
        
        

region = gpd.read_file('data/master-plan-2019-region-boundary-no-sea-kml-polygon.shp')

polygons=[region.iloc[0]["geometry"],
          region.iloc[1]["geometry"],
          region.iloc[2]["geometry"],
          region.iloc[3]["geometry"],
          region.iloc[4]["geometry"]]

union_poly = unary_union(polygons)
boundary = gpd.GeoSeries(union_poly)
boundary.crs="epsg:4326"
boundary.plot()
plt.show()

df=pd.read_csv('data/mcd.csv',header=None)

mcd_gdf=gpd.GeoDataFrame()
mcd_gdf['name_list_1']=df.iloc[0::3,:][0].reset_index(drop=True)
mcd_gdf['name_list_2']=df.iloc[1::3,:][0].reset_index(drop=True)
mcd_gdf['postcode']=df.iloc[2::3,:][0].reset_index(drop=True)
mcd_gdf['query']=mcd_gdf['name_list_2'] + str(", ") + mcd_gdf['postcode'] 
mcd_gdf['sn']=np.arange(len(mcd_gdf))
geometry_list=[]
json_list=[]
country_list=[]


for i in tqdm(range(len(mcd_gdf))):
    url= "http://api.positionstack.com/v1/forward?access_key=0165d4692a756c1106d62c3c402bca43&query="+str(mcd_gdf['query'].iloc[i])+"&country=SG&limit=50"
    jsondata=requests.get(url).json()
    # if(len(jsondata['data'])==0):
    #     url= "http://api.positionstack.com/v1/forward?access_key=0165d4692a756c1106d62c3c402bca43&query="+str(mcd_gdf['postcode'].iloc[i])+"&country=SG&limit=50"
    #     jsondata=requests.get(url).json()
    print(mcd_gdf['query'].iloc[i])
    json_list.append(jsondata)
    try:
        geometry_list.append(Point(jsondata['data'][0]['longitude'],jsondata['data'][0]['latitude']))
        country_list.append(jsondata['data'][0]['country'])
    except:
        print('Not Found')
        geometry_list.append(np.nan)
        country_list.append(np.nan)




mcd_gdf['geometry']=geometry_list
mcd_gdf['country']=country_list
mcd_gdf['json_data']=json_list

mcd_gdf_1=mcd_gdf[mcd_gdf['country']=='Singapore']

#second_pass
mcd_gdf_2=mcd_gdf[mcd_gdf['country']!='Singapore']
mcd_gdf_2['query']=mcd_gdf_2['name_list_1'] + str(", ") + mcd_gdf_2['name_list_2'] + str(", ") + mcd_gdf_2['postcode'] 

for i in range(len(mcd_gdf_2)):
    url= "http://api.positionstack.com/v1/forward?access_key=0165d4692a756c1106d62c3c402bca43&query="+str(mcd_gdf_2['query'].iloc[i])+"&country=SG&limit=50"
    # print(url)
    jsondata=requests.get(url).json()
    mcd_gdf_2['json_data'].iloc[i]=str(jsondata)
    try:
        mcd_gdf_2['geometry'].iloc[i]=Point(jsondata['data'][0]['longitude'],jsondata['data'][0]['latitude'])
        mcd_gdf_2['country'].iloc[i]=jsondata['data'][0]['country']
        
    except:
        print('Not Found')
        mcd_gdf_2['geometry'].iloc[i]=np.nan
        mcd_gdf_2['country'].iloc[i]=np.nan





mcd_gdf_2_pass=mcd_gdf_2[mcd_gdf_2['country']=='Singapore']
#thirdpass
mcd_gdf_3=mcd_gdf_2[mcd_gdf_2['country']!='Singapore']

mcd_gdf_3['query']=mcd_gdf_3['name_list_2'].str.split('#').map(lambda x: x[0]) + str(", ") + mcd_gdf_3['postcode'] 

for i in range(len(mcd_gdf_3)):
    url= "http://api.positionstack.com/v1/forward?access_key=0165d4692a756c1106d62c3c402bca43&query="+str(mcd_gdf_3['query'].iloc[i])+"&country=SG&limit=50"
    # print(url)
    jsondata=requests.get(url).json()
    mcd_gdf_3['json_data'].iloc[i]=str(jsondata)
    try:
        mcd_gdf_3['geometry'].iloc[i]=Point(jsondata['data'][0]['longitude'],jsondata['data'][0]['latitude'])
        mcd_gdf_3['country'].iloc[i]=jsondata['data'][0]['country']
        
    except:
        print('Not Found')
        mcd_gdf_3['geometry'].iloc[i]=np.nan
        mcd_gdf_3['country'].iloc[i]=np.nan



mcd_gdf_3_pass=mcd_gdf_3[mcd_gdf_3['country']=='Singapore']

#lastpass_manual
mcd_gdf_4=mcd_gdf_3[mcd_gdf_3['country']!='Singapore']

mcd_gdf_4['geometry'] = Point(103.802092,1.30415)
mcd_gdf_4['country']='Singapore'
mcd_gdf_4['json_data'] = str({
    "data": [
        {
            "latitude": 1.30415,
            "longitude": 103.802092,
            "type": "address",
            "name": "580 Queensway",
            "number": "580",
            "postal_code": "null",
            "street": "Queensway",
            "confidence": 1,
            "region": "Central Singapore",
            "region_code": "CS",
            "county": "null",
            "locality": "Singapore",
            "administrative_area": "null",
            "neighbourhood": "null",
            "country": "Singapore",
            "country_code": "SGP",
            "continent": "Asia",
            "label": "580 Queensway, Singapore",
            "bbox_module": [],
            "country_module": {
                "latitude": 1.3219958543777466,
                "longitude": 103.8205337524414,
                "common_name": "Singapore",
                "official_name": "Republic of Singapore",
                "capital": "Singapore",
                "flag": "🇸🇬",
                "area": 710,
                "landlocked": "false",
                "independent": "true",
                "global": {
                    "alpha2": "SG",
                    "alpha3": "SGP",
                    "numeric_code": "702",
                    "region": "Asia",
                    "subregion": "South-Eastern Asia",
                    "region_code": "142",
                    "subregion_code": "035",
                    "world_region": "APAC",
                    "continent_name": "Asia",
                    "continent_code": "AS"
                },
                "dial": {
                    "calling_code": "65",
                    "national_prefix": "null",
                    "international_prefix": "001"
                },
                "currencies": [
                    {
                        "symbol": "$",
                        "code": "SGD",
                        "name": "Singapore Dollar",
                        "numeric": 702,
                        "minor_unit": 2
                    }
                ],
                "languages": {
                    "zho": "Chinese",
                    "eng": "English",
                    "msa": "Malay",
                    "tam": "Tamil"
                }
            },
            "sun_module": {
                "rise": {
                    "time": 1637362118,
                    "astronomical": 1637357741,
                    "civil": 1637360805,
                    "nautical": 1637359275
                },
                "set": {
                    "time": 1637405528,
                    "astronomical": 1637409905,
                    "civil": 1637406841,
                    "nautical": 1637408371
                },
                "transit": 1637383823
            },
            "timezone_module": {
                "name": "Asia/Singapore",
                "offset_sec": 28800,
                "offset_string": "+08:00"
            }
        }
    ]
})

mcd_gdf_master=pd.concat([mcd_gdf_1,mcd_gdf_2_pass,mcd_gdf_3_pass,mcd_gdf_4])

mcd_gdf_master.sort_values(by=['sn'],inplace=True)


mcd_gdf_master.crs="epsg:4326"


fig, ax = plt.subplots(figsize=(12, 10))
boundary.plot(ax=ax,color='gray')
mcd_gdf_master.plot(ax=ax,markersize=3.5, color='black')
ax.axis('off')
ax.ticklabel_format(useOffset=False)
plt.show()


boundary = boundary.to_crs(epsg=3395)
gdf_proj = mcd_gdf_master.to_crs(boundary.crs)

boundary_shape = cascaded_union(boundary.geometry)
coords = points_to_coords(gdf_proj.geometry)



poly_shapes,pts = voronoi_regions_from_coords(coords, boundary_shape)
# fig, ax = subplot_for_map()
fig, ax = plt.subplots(figsize=(18,12))
plot_voronoi_polys_with_points_in_area(ax, boundary_shape, poly_shapes, coords,pts,points_markersize=20)
ax.set_title('Voronoi regions of MCD in Singapore')
plt.tight_layout()
ax.axis('off')
ax.ticklabel_format(useOffset=False)
plt.show()




region_elec = gpd.read_file('data/electoral-boundary-dataset-polygon.shp')

region_elec.plot()
plt.tight_layout()
ax.axis('off')
ax.ticklabel_format(useOffset=False)
plt.show()
