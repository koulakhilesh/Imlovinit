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
sns.set_theme()
import requests
from tqdm import tqdm
from shapely.geometry import Point
from shapely.ops import cascaded_union
from shapely.ops import unary_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords



class imlovint():
    
    def __init__(self,chain='MCD',sg_region_shape='master-plan-2019-region-boundary-no-sea-kml-polygon.shp',notebook=True):
        
        if notebook== False:
            self.sg_region_shape_path='../data/'+sg_region_shape
            self.data_path='../data/'
            if chain=='MCD':
                self.image_path='../data/MCD.png' 
        if notebook== True:
             self.sg_region_shape_path='data/'+sg_region_shape
             self.data_path='data/' 
             if chain=='MCD':
                 self.image_path='data/MCD.png' 
        
        
        self.chain=chain    
        self.getBoundary()
        self.getShape()
            
    def getBoundary(self,plot=False): 
        region = gpd.read_file(self.sg_region_shape_path)
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

    def getShape(self):
        if self.chain=='MCD':
            self.chain_gdf = gpd.read_file(self.data_path+'mcd_gdf.shp')
        


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
    
        


        
        
        
        
if __name__ == '__main__':
    imlovint_class=imlovint(notebook=False)
    # imlovint_class.getBoundary(plot=True)
    # imlovint_class.justDots()
    imlovint_class.drawVoronoi()
       
# arr_image = plt.imread('../data/MCD.png', format='png')
    

# fig, ax = plt.subplots(figsize=(12,8))


# im = Image.open(')

# height = im.size[1]

# # We need a float array between 0-1, rather than
# # a uint8 array between 0-255
# im = np.array(im).astype(np.float) / 255

# fig = plt.figure()

# plt.plot(np.arange(10), 4 * np.arange(10))

# # With newer (1.0) versions of matplotlib, you can 
# # use the "zorder" kwarg to make the image overlay
# # the plot, rather than hide behind it... (e.g. zorder=10)
# fig.figimage(im, 0, fig.bbox.ymax - height)

# # (Saving with the same dpi as the screen default to
# #  avoid displacing the logo image)
# fig.savefig('/home/jofer/temp.png', dpi=80)

# plt.show()


