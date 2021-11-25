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
import sys
sys.path.append("..")
import seaborn as sns
sns.set_theme()
import requests
from tqdm import tqdm
from shapely.geometry import Point
from shapely.ops import cascaded_union
from shapely.ops import unary_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords
from data.db_description import getDatabase




class imlovint():
    
    def __init__(self,chain='MCD',notebook=True):
        
        
       
        chainDB=getDatabase()
        regionDB=next(item for item in chainDB if item['Name'] == 'MASTER_PLAN')  
        attrDB=next(item for item in chainDB if item['Name'] == chain)
         
        if notebook== False:
         
            self.shape_path='../'
            self.image_path='../'+attrDB['logoFile']
            
        if notebook== True:
         
              self.shape_path='' 
              self.image_path=attrDB['logoFile']
            
        self.chain=chain    
        self.getBoundary(regionDB)
        self.getShape(chain)
            
    def getBoundary(self,regionDB,plot=False): 
        
        region = gpd.read_file(self.shape_path + regionDB['shapeFile'])
        polygons=[region.iloc[0]["geometry"],
                  region.iloc[1]["geometry"],
                  region.iloc[2]["geometry"],
                  region.iloc[3]["geometry"],
                  region.iloc[4]["geometry"]]

        union_poly = unary_union(polygons)
        self.boundary = gpd.GeoSeries(union_poly)
        self.boundary.crs="epsg:4326"
        if plot==True:
            fig, ax = plt.subplots(figsize=(12, 8))
            self.boundary.plot(ax=ax,color='gray')
            ax.axis('off')
            plt.show()

    def getShape(self,chain):
        
        chainDB=getDatabase()
        attrDB=next(item for item in chainDB if item['Name'] == chain)
        self.chain_gdf = gpd.read_file(self.shape_path+attrDB['shapeFile'])



    def justDots(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        self.boundary.plot(ax=ax,color='gray')
        self.chain_gdf.plot(ax=ax,markersize=3.5, color='black')
        ax.axis('off')
        plt.show()
    
    def drawVoronoi(self):
        self.boundary = self.boundary.to_crs(epsg=3395)
        gdf_proj = self.chain_gdf.to_crs(self.boundary.crs)

        boundary_shape = cascaded_union(self.boundary.geometry)
        coords = points_to_coords(gdf_proj.geometry)

        poly_shapes,pts = voronoi_regions_from_coords(coords, boundary_shape)
        # fig, ax = subplot_for_map()
        
        arr_image = plt.imread(self.image_path, format='png')
        fig, ax = plt.subplots(figsize=(7/4,1))
        ax.axis('off')
        ax.imshow(arr_image)
        plt.show()

        fig, ax = plt.subplots(figsize=(12,8))
        
        plot_voronoi_polys_with_points_in_area(ax, boundary_shape, poly_shapes, coords,pts,points_markersize=20)
        ax.set_title('Voronoi regions for '+str(self.chain) +' chain in Singapore',fontsize=15)
        plt.tight_layout()
        ax.axis('off')
        plt.show()
    
    
        
    def getNearby(self,address='Marina Bay Sands',distance=0.03):
        url='https://developers.onemap.sg/commonapi/search?searchVal='+str(address)+'&returnGeom=Y&getAddrDetails=Y&pageNum=1'
        jsondata=requests.get(url).json()
        
        if len(jsondata['results'])>0:
            print('Found '+str(len(jsondata['results']))+ ' results, using the first default one')
            print(str(jsondata['results'][0]['ADDRESS']))
            lat=float(jsondata['results'][0]['LATITUDE'])
            long=float(jsondata['results'][0]['LONGITUDE'])
            # print(long,lat)
            
            local=gpd.GeoDataFrame()
            geoser=gpd.GeoDataFrame([Point(long,lat)])
            local['geometry']=geoser[0]
            
            local_buffer=gpd.GeoDataFrame()
            local_buffer['geometry']=local.buffer(distance)
            local_buffer.crs="epsg:4326"
            
          
            bool_list=[]
            for i in range(len(self.chain_gdf)):
                bool_list.append(local_buffer.contains(self.chain_gdf.iloc[i]['geometry']).item())
            
            nearbyDF=pd.DataFrame()
            if(any(ele for ele in bool_list)==True):
                
                chain_inlocal=[i for i, x in enumerate(bool_list) if x]
                print('\n'+str(len(chain_inlocal))+' chain Found')
                for j in range(len(chain_inlocal)):
                    nearbyDF=nearbyDF.append(self.chain_gdf.iloc[chain_inlocal[j]])
                    
                    # print(pd.DataFrame(self.chain_gdf.iloc[chain_inlocal[j]]))
                
           
            
               
            else:
                print("\nNo chain found at the given address")
            self.boundary = self.boundary.to_crs(epsg=3395)
            gdf_proj = self.chain_gdf.to_crs(self.boundary.crs)
            local_buffer_proj = local_buffer.to_crs(self.boundary.crs)

            boundary_shape = cascaded_union(self.boundary.geometry)
            coords = points_to_coords(gdf_proj.geometry)

            poly_shapes,pts = voronoi_regions_from_coords(coords, boundary_shape)
            # fig, ax = subplot_for_map()
            
            arr_image = plt.imread(self.image_path, format='png')
            fig, ax = plt.subplots(figsize=(7/4,1))
            ax.axis('off')
            ax.imshow(arr_image)
            plt.show()

            fig, ax = plt.subplots(figsize=(12,8))
            
            plot_voronoi_polys_with_points_in_area(ax, boundary_shape, poly_shapes, coords,pts,points_markersize=20)
            local_buffer_proj.plot(ax=ax,color='red',edgecolor='black',alpha=0.5)
            ax.set_title('Voronoi regions for '+str(self.chain) +' chain in Singapore, with location radius of 3kms',fontsize=15)
            plt.tight_layout()
            ax.axis('off')
            plt.show()
            
            nearbyDF.reset_index(drop=True,inplace=True)
            # print(nearbyDF.head()) 
            return nearbyDF
           
            
            
        
        
        
        
if __name__ == '__main__':
    imlovint_class=imlovint(chain='MUSEUMS',notebook=False)
    # imlovint_class.getBoundary(plot=True)
    # imlovint_class.justDots()
    # imlovint_class.drawVoronoi()
    nearbyDF=imlovint_class.getNearby(address='Bukit Timah' , distance=0.03)
    
      

   # 'MCD' :  ok    
   # 'LIBRARY': ok
   # 'MUSEUMS'  : ok
       