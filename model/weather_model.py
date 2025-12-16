import pandas as pd
import requests
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt

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
        return pd.json_normalize(response['features'])

    def data_behandling(self):
        to_drop =[
            'geometry.type',
            'id',
            'properties.parameterId',
            'properties.created',
            'geometry.coordinates',
            'properties.stationId',
            'type'
        ]
        df = self.get_temperature_data()
        return df.drop(to_drop, inplace=False, axis=1)


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
    
    def format_time(self):
        df = self.data_behandling()

        y = list(df['properties.value'])
        x = []
        z = []

        # formats the times, by removing unnececary information
        for i in df['properties.observed']:
            x = i[11:]
            z.append(x[:5])

        times = []
        # Reverse the lists, because else it will be displayed in reverse
        for j in range(len(z)):
            times.append(z[j])
        times.reverse()
        y.reverse()

        ticks = []
        other = 0
        # Takes only the times when it is a full hour. We also only take every other hour so it doesn't look as cluttered
        for k in times:
            if k[3:] == '00':
                if other == 0:
                    ticks.append(k)
                    other = 1
                else:
                    other -= 1
        return ticks, y
