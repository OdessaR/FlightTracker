from flask import Flask, request, jsonify, render_template
import json
from flightapi import FlightInfoFetcher

app = Flask(__name__)

fetcher = FlightInfoFetcher()
airline_name = ""

@app.route('/')
def index():
    # Render the HTML page with the dropdown
    return render_template('index.html')

@app.route('/airlines', methods=['GET'])
def get_airlines():
    with open('airline_icao.json') as f:
        airlines = json.load(f)
    return jsonify(airlines)

@app.route("/aircrafts_per_airline/<airline_icao>", methods = ['GET'])
def feed_aircrafts(airline_icao):
    data = fetcher.fr_call_get_flights_per_airline(airline_icao)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
