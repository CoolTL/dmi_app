import pandas as pd
import requests

class WeatherModel:
    """
    Model-laget henter og forarbejder data fra DMI Open Data.
    Returnerer data i et format, der er klar til plotting.
    """

    def get_temperature_data(self):
        # TODO: Udskift med ægte DMI API kald
        # Eksempel på dummy-data:
        data = [
            {"name": "København", "lat": 55.6761, "lon": 12.5683, "temp": 6.4},
            {"name": "Aarhus", "lat": 56.1629, "lon": 10.2039, "temp": 5.7},
            {"name": "Odense", "lat": 55.4038, "lon": 10.4024, "temp": 6.0},
        ]
        return pd.DataFrame(data)

    def fetch_from_dmi(self, endpoint):
        pass
