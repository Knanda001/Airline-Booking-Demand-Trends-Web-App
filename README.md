# Airline Booking Demand Trends Web App

## Overview
This is a Python web application built with Flask to fetch and analyze airline booking demand trends using the Aviationstack API. It displays popular routes, demand by date, and a visualization of route popularity for a given airport code.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Knanda001/Airline-Booking-Demand-Trends-Web-App.git
   cd Airline-Booking-Demand-Trends-Web-App
   ```

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed. Then, install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an Aviationstack API Key**:
   - Sign up for a free account at [aviationstack.com](https://aviationstack.com).
   - Copy your API key and replace `YOUR_API_KEY_HERE` in `app.py` with your key.

4. **Run the Application**:
   ```bash
   python app.py
   ```
   The app will run locally at `http://127.0.0.1:5000`.

5. **Usage**:
   - Open the URL in a browser.
   - Enter an IATA airport code (e.g., SYD for Sydney) and click "Fetch Data".
   - View tables of popular routes and demand by date, plus a bar chart of route popularity.

## Features
- **Data Scraping**: Fetches real-time flight data from Aviationstack API.
- **Data Processing**: Analyzes flight data to identify popular routes and high-demand periods.
- **Visualization**: Displays a bar chart of top routes using Plotly.
- **User Interface**: Simple Flask-based web interface with input for airport code and tabulated/chart outputs.

## Notes
- The Aviationstack free tier limits to 100 API requests/month. Be mindful of usage.
- The app focuses on flight frequency as a proxy for demand due to limited pricing data in free APIs.
- For production, consider a paid API or additional data sources for pricing trends.

## Future Improvements
- Add more filters (e.g., date range, destination).
- Integrate additional APIs (e.g., Skyscanner) for pricing data.
- Deploy to a cloud platform (e.g., Heroku) for accessibility.
- Enhance analytics with machine learning for demand forecasting.