# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# reflect an existing database into a new model

# reflect the tables
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    """Return the JSON representation of the last 12 months of precipitation data."""
    # Calculate the date 1 year ago from the last data point in the database
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_date = dt.datetime.strptime(latest_date, "%Y-%m-%d")
    one_year_ago = latest_date - dt.timedelta(days=365)
    
    # Query for the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    
    # percipitation_data = {}
    # for date, prcp in results:
    #     percipitation_data[date] = prcp
    
    session.close()
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """Return a JSON list of stations from the dataset."""
    results = session.query(Station.station).all()
    station_list = [station[0] for station in results]
   session.close()

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    """Return a JSON list of temperature observations for the previous year."""
    # Find the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]
    
    # Calculate the date 1 year ago from the last data point in the database
    last_date = session.query(func.max(Measurement.date)).scalar()
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    one_year_ago = last_date - dt.timedelta(days=365)
    
    # Query for the temperature observations of the most active station for the previous year
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station).\
        filter(Measurement.date >= one_year_ago).all()
    
    # Create a list of dictionaries
    temperature_data = [{"date": date, "temperature": tobs} for date, tobs in results]
    
    return jsonify(temperature_data)

@app.route("/api/v1.0/<start>")
def start_date_stats(start):
    session = Session(engine)

    """Return a JSON list of the minimum temperature, average temperature, and maximum temperature for dates greater than or equal to the start date."""
    # Convert the start date to a datetime object
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    
    # Query for TMIN, TAVG, and TMAX for dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    
    # Create a dictionary with the result values
    start_date_stats_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    
    return jsonify(start_date_stats_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date_stats(start, end):
    """Return a JSON list of the minimum temperature, average temperature, and maximum temperature for the specified date range."""
    # Convert the start and end dates to datetime objects
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    
    # Query for TMIN, TAVG, and TMAX for dates within the specified range
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    
    # Create a dictionary with the result values
    start_end_date_stats_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    
    return jsonify(start_end_date_stats_data)

if __name__ == "__main__":
    app.run(debug=True)