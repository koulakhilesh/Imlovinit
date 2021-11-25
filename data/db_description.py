#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def getDatabase():
    
    
    region_db=[]
    masterPlan={'Name':'MASTER_PLAN',
         'Description':'Master Plan 2019 Region Boundary (No Sea)',
         'Remarks':'Converted from .kml to .shp',
         'logoFile':'NA',
         'shapeFile':'data/shapeFiles/masterPlan/master-plan-2019-region-boundary-no-sea-kml-polygon.shp',
         'Source':'Urban Redevelopment Authority',
         'LastUpdated':'13-08-2020',
         'License':'https://data.gov.sg/open-data-licence'
         }
    
    region_db.append(masterPlan)
    
    db_dict=[]
    mcd={'Name':'MCD',
         'Description':'List of MCD outlets in Singpore',
         'Remarks':'NA',
         'logoFile':'data/logoFiles/MCD.png',
         'shapeFile':'data/shapeFiles/mcd/mcd_gdf.shp',
         'Source':'https://www.mcdonalds.com.sg/locate-us/',
         'LastUpdated':'20-11-2021',
         'License':'NA'
         }
    
    db_dict.append(mcd)
    
    library={'Name':'LIBRARY',
         'Description':'List of Library location in Sinagpore',
         'Remarks':'Converted from .kml to .shp',
         'logoFile':'data/logoFiles/LIBRARY.png',
         'shapeFile':'data/shapeFiles/library/libraries-point.shp',
         'Source':'National Library Board',
         'LastUpdated':'25-08-2021',
         'License':'https://data.gov.sg/open-data-licence'
         }
    
    db_dict.append(library)
    
    museums={'Name':'MUSEUMS',
         'Description':'List of Museums location in Sinagpore',
         'Remarks':'Converted from .kml to .shp',
         'logoFile':'data/logoFiles/MUSEUMS.png',
         'shapeFile':'data/shapeFiles/museums/museums-kml-point.shp',
         'Source':'National Heritage Board',
         'LastUpdated':'24-01-2019',
         'License':'https://data.gov.sg/open-data-licence'
         }
    
    db_dict.append(museums)
    
    e_waste={'Name':'E_WASTE',
         'Description':'List of E-waste recycling near you',
         'Remarks':'Converted from .kml to .shp',
         'logoFile':'data/logoFiles/EWASTE.png',
         'shapeFile':'data/shapeFiles/e_waste/e-waste-recycling-kml-point.shp',
         'Source':'National Environment Agency',
         'LastUpdated':'02-10-2021',
         'License':'https://data.gov.sg/open-data-licence'
         }
    
    db_dict.append(e_waste)
    
    wireless_hs={'Name':'WIRELESS_HS',
          'Description':'List of Wireless@SG hotspots in Singapore',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/HOTSPOT.png',
          'shapeFile':'data/shapeFiles/wireless-hotspots/wireless-hotspots-geojson.shp',
          'Source':'Infocomm Media Development Authority',
          'LastUpdated':'22-03-2020',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(wireless_hs)
    
    
    waste_treatment={'Name':'WASTE_TREATMENT',
          'Description':'Location of Toxic Industrial Wastes Treatment and Disposal Facilities',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/WASTE.png',
          'shapeFile':'data/shapeFiles/waste-treatment/waste-treatment-geojson.shp',
          'Source':'NATIONAL ENVIRONMENT AGENCY',
          'LastUpdated':'22-03-2020',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(waste_treatment)
    
    monuments={'Name':'MONUMENTS',
          'Description':'List of locations of monuments in Sinagpore',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/MONUMENTS.png',
          'shapeFile':'data/shapeFiles/monuments/monuments-geojson.shp',
          'Source':'National Heritage Board',
          'LastUpdated':'24-01-2019',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(monuments)
    
    historic_sites={'Name':'HISTORIC_SITES',
          'Description':'List of locations of Historic Sites in Sinagpore',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/HISTORIC.png',
          'shapeFile':'data/shapeFiles/historic_sites/historic-sites-geojson.shp',
          'Source':'National Heritage Board',
          'LastUpdated':'24-01-2019',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(historic_sites)
    
    heritage_trees={'Name':'HERITAGE_TREES',
          'Description':'List of locations of Heritage trees Sites in Sinagpore',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/HERITAGE.png',
          'shapeFile':'data/shapeFiles/heritage_trees/heritage-trees-geojson.shp',
          'Source':'NATIONAL PARKS BOARD',
          'LastUpdated':'10-06-2020',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(heritage_trees)
    
    hawker_centres={'Name':'HAWKER_CENTRE',
          'Description':'List of locations of Hawker Center in Sinagpore',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/HAWKER.png',
          'shapeFile':'data/shapeFiles/hawker_centres/hawker-centres-geojson.shp',
          'Source':'NATIONAL ENVIRONMENT AGENCY',
          'LastUpdated':'03-09-2021',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(hawker_centres)
    
    dsa={'Name':'DSA',
          'Description':'List of locations of Designated Smoking Areas (DSA)',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/DSA.png',
          'shapeFile':'data/shapeFiles/dsa/designated-smoking-areas-geojson.shp',
          'Source':'National Environment Agency',
          'LastUpdated':'09-09-2021',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(dsa)
    
        
    cft={'Name':'CFT',
          'Description':'List of locations of Cash For Trash stations near you',
          'Remarks':'Converted from .geojson to .shp',
          'logoFile':'data/logoFiles/CFT.png',
          'shapeFile':'data/shapeFiles/cft/cash-for-trash-geojson.shp',
          'Source':'NATIONAL ENVIRONMENT AGENCY',
          'LastUpdated':'06-03-2021',
          'License':'https://data.gov.sg/open-data-licence'
          }
 
    db_dict.append(cft)
    
    
    return region_db,db_dict


# if __name__ == '__main__':

#     # db_dict=getDatabase()
    
    

