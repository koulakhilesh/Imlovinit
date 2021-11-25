#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:28:15 2021

@author: ess_admin
"""

# from osgeo import 

import geopandas as gpd
import fiona
fiona.supported_drivers

# fiona.drvsupport.supported_drivers['kml'] = 'rw' # enable KML support which is disabled by default
# fiona.drvsupport.supported_drivers['KML'] = 'rw' # enable KML support which is disabled by default

# fiona.drvsupport.supported_drivers['libkml'] = 'rw' # enable KML support which is disabled by default
# fiona.drvsupport.supported_drivers['LIBKML'] = 'rw' # enable KML support which is disabled by default

a = gpd.read_file("wireless-hotspots-geojson.geojson")

a.to_file('wireless-hotspots-kml.shp',driver='ESRI Shapefile')
