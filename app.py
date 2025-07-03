from flask import Flask, render_template, request
import requests
import pandas as pd
import plotly.express as px
import plotly.io as pio
from collections import Counter
from datetime import datetime, timedelta

app = Flask(__name__)


API_KEY = "6d8f30fdbe87ab2d0fd8707cb0ca76dc"  
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_flight_data(airport_code=None):
    params = {
        "access_key": API_KEY,
        "limit": 100  # Free tier limit
    }
    if airport_code:
        params["dep_iata"] = airport_code  # Filter by departure airport
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json().get("data", [])
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def process_flight_data(flights):
    if not flights:
        return None, None, None
    
    # Extract relevant fields
    routes = []
    dates = []
    for flight in flights:
        if flight.get("departure", {}).get("iata") and flight.get("arrival", {}).get("iata"):
            route = f"{flight['departure']['iata']} -> {flight['arrival']['iata']}"
            routes.append(route)
            # Parse scheduled departure time
            if flight.get("departure", {}).get("scheduled"):
                date = flight["departure"]["scheduled"].split("T")[0]
                dates.append(date)
    
    # Analyze popular routes
    route_counts = Counter(routes).most_common(5)  # Top 5 routes
    routes_df = pd.DataFrame(route_counts, columns=["Route", "Flight Count"])
    
    # Analyze demand by date
    date_counts = Counter(dates).most_common(5)  # Top 5 dates
    dates_df = pd.DataFrame(date_counts, columns=["Date", "Flight Count"])
    
    # Create Plotly bar chart for routes
    fig = px.bar(routes_df, x="Route", y="Flight Count", title="Top 5 Popular Routes")
    fig.update_layout(xaxis_title="Route", yaxis_title="Number of Flights")
    plot_html = pio.to_html(fig, full_html=False)
    
    return routes_df, dates_df, plot_html

@app.route("/", methods=["GET", "POST"])
def index():
    routes_df = None
    dates_df = None
    plot_html = None
    airport_code = None
    
    if request.method == "POST":
        airport_code = request.form.get("airport_code", "").upper()
        flights = fetch_flight_data(airport_code)
        routes_df, dates_df, plot_html = process_flight_data(flights)
    
    return render_template("index.html", routes_df=routes_df, dates_df=dates_df, 
                         plot_html=plot_html, airport_code=airport_code)

if __name__ == "__main__":
    app.run(debug=True)