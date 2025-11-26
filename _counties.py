# Get county lookup data from ArcGIS REST API

import requests
import pandas as pd

def get_counties_df():
    url = (
        "https://services1.arcgis.com/99lidPhWCzftIe9K/ArcGIS/rest/services/"
        "UtahCountyBoundaries/FeatureServer/0/query"
    )

    params = {
        "where": "1=1",
        "outFields": "*",
        "f": "json"
    }

    data = requests.get(url, params=params).json()
    df = pd.DataFrame([f["attributes"] for f in data["features"]])

    df.columns = df.columns.str.upper()
    df.rename(columns={"NAME": "CO_NAME", "FIPS": "CO_FIPS"}, inplace=True)

    return df[['CO_FIPS','CO_NAME']]
