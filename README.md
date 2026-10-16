# NJ Warehouse Sprawl and Truck Pollution

This project maps where warehouses have grown along the NJ Turnpike corridor (Middlesex, Union, and Essex counties) using aerial imagery from 2010 onward, estimates how busy they are by counting truck trailers and loading docks with computer vision, and tests whether that activity is associated with higher NO2 and PM2.5 and with asthma ER visits in nearby neighborhoods, especially overburdened communities.

## Current status

Manually labeling the training data

## Data sources

All sources are free and public. (10/19/26)

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
| Census county population estimates | https://www2.census.gov/programs-surveys/popest/datasets/ |
| Census tract boundaries (TIGER) | https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_34_tract.zip |
| NJDEP Overburdened Communities | https://services1.arcgis.com/QWdNfRs7lkPq4g4Q/arcgis/rest/services/Overburdened_Communities_under_the_New_Jersey_Environmental_Justice_Law/FeatureServer/19 |
| EJScreen 2.3 (archived after EPA took it offline in Feb 2025) | https://doi.org/10.7910/DVN/RLR5AX |

## License

The code in this repository is released under the [MIT License](LICENSE).

The data is not covered by the MIT License; each source keeps its own terms:

- **Public domain (U.S. federal government):** NAIP, Census ACS, TIGER, and population estimates; EPA AQS, FAQSD, and EJScreen; FHWA HPMS.
- **OpenStreetMap and Microsoft Building Footprints:** [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/). Any published dataset derived from them, including this project's warehouse inventory, is released under the ODbL.
- **ACAG satellite PM2.5:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Sentinel-5P TROPOMI:** free and open under the Copernicus data policy, with attribution.
- **New Jersey state data (NJOGIS, NJDEP, NJSHAD):** used under each agency's public data terms; the State of New Jersey does not endorse this project.

### Attribution

- Map data © OpenStreetMap contributors, available under the ODbL.
- Building footprints © Microsoft, available under the ODbL.
- Contains modified Copernicus Sentinel data, processed by ESA and the European Commission.
- Surface PM2.5: Atmospheric Composition Analysis Group, Washington University in St. Louis (SatPM2.5 V6.GL).
