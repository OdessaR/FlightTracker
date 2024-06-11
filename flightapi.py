from FlightRadar24 import FlightRadar24API
import json

fr_api = FlightRadar24API()

# configurations for flight radar api
flight_tracker_config = fr_api.get_flight_tracker_config()
flight_tracker_config.limit = 5000
flight_tracker_config.gliders = "0"
flight_tracker_config.gnd = "0"
flight_tracker_config.vehicles = "0"

fr_api.set_flight_tracker_config(flight_tracker_config)

class FlightInfoFetcher():
    def __init__(self):
        pass
    def fr_call_get_flights_per_airline(self, airline_icao):
        flights = fr_api.get_flights(airline_icao)
        geojson = {
            "type": "FeatureCollection",
            "features":[
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [flight.longitude, flight.latitude],
                    },
                    "properties":{
                        "name": flight.registration,
                        "rotation": flight.heading,
                        "icon": "https://openclipart.org/image/400px/4108",
                    },
                } for flight in flights
            ]
        }

        with open ('data/aircrafts.geojson','w') as f:
            json.dump(geojson, f)
        return geojson

fetcher = FlightInfoFetcher()
fetcher.fr_call_get_flights_per_airline("KLM")