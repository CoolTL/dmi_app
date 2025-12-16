import pandas as pd
import requests
from datetime import datetime, timedelta, timezone

class WeatherModel:
    """
    Model-laget henter og forarbejder data fra DMI Open Data.
    Returnerer data i et format, der er klar til plotting.
    """

    def __init__(self):
        """Set up time variables"""
        hours = 24
        now = datetime.now(timezone.utc)
        start = now - timedelta(hours=hours)
        self.datetime_range = f"{start.isoformat()}/{now.isoformat()}"
        

    def get_temperature_data(self):
        # Get data from DMI
        response = self.fetch_from_dmi()
        df = pd.json_normalize(response['features'])
        #return pd.DataFrame(data)

    def fetch_from_dmi(self):
        # Url and params for fetching data
        url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items"
        params = {
    "api-key": "75ab0b53-550a-4ede-b9ae-d1d9bc108f48",   # <- indsæt din egen nøgle
    "stationId": "06081",       # station fx København
    "parameterId": "temp_dry",  # parameter fx temperatur
    "datetime": self.datetime_range,
    "limit": 1000
}
        return requests.get(url, params=params).json()
    
