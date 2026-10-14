# NJ Warehouse Sprawl and Truck Pollution

About one in three New Jersey residents lives within half a mile of a large warehouse, yet warehouses fall outside the state's Environmental Justice Law. This project maps where warehouses have grown along the NJ Turnpike corridor (Middlesex, Union, and Essex counties) using aerial imagery from 2010 onward, estimates how busy they are by counting truck trailers and loading docks with computer vision, and tests whether that activity is associated with higher NO2 and PM2.5 and with asthma ER visits in nearby neighborhoods, especially overburdened communities. The end product is an open, interactive map where anyone can look up a town and see nearby warehouse growth, truck activity, and air quality.

## Data sources

All sources are free and public.

| Data | Source |
|---|---|
| County boundaries (Census TIGER) | https://developers.google.com/earth-engine/datasets/catalog/TIGER_2018_Counties |
| NAIP aerial imagery | https://planetarycomputer.microsoft.com/dataset/naip |
| OpenStreetMap buildings and industrial land use | https://overpass-api.de/api/interpreter |
| Microsoft Building Footprints | https://minedbuildings.z5.web.core.windows.net/global-buildings/dataset-links.csv |
| Parcels and MOD-IV tax records (NJOGIS) | https://services2.arcgis.com/XVOqAjTOJ5P6ngMu/arcgis/rest/services/Parcels_Composite_NJ_WM/FeatureServer/0 |
| Truck traffic (FHWA HPMS, from NJDOT counts) | https://geo.dot.gov/server/rest/services/Hosted/HPMS_FULL_NJ_2024/FeatureServer/0 |
| Sentinel-5P TROPOMI NO2 | https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2 |
| NJDEP / EPA ground monitors (AQS) | https://aqs.epa.gov/aqsweb/airdata/download_files.html |
| EPA FAQSD daily PM2.5 by census tract | https://www.epa.gov/hesc/rsig-related-downloadable-data-files |
| Satellite-derived PM2.5, ACAG V6.GL (~1 km) | https://sites.wustl.edu/acag/datasets/surface-pm2-5/ |
| Asthma ER visits (NJSHAD) | https://www-doh.nj.gov/doh-shad/ |
| Census ACS 5-year | https://api.census.gov/data/2024/acs/acs5 |
| Census tract boundaries (TIGER) | https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_34_tract.zip |
| NJDEP Overburdened Communities | https://services1.arcgis.com/QWdNfRs7lkPq4g4Q/arcgis/rest/services/Overburdened_Communities_under_the_New_Jersey_Environmental_Justice_Law/FeatureServer/19 |
| EJScreen 2.3 (archived after EPA took it offline in Feb 2025) | https://doi.org/10.7910/DVN/RLR5AX |
