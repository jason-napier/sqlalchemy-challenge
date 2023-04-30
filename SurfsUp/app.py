# Import the dependencies.
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
station = Base.classes.station
measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return f'''
    Welcome to the homepage! \n
    Available Routes: \n
    /api/v1.0/precipitation \n
        #Dates and Precipitation over the last 12 months of data. \n

    /api/v1.0/stations\n
        #List of stations\n
    
    /api/v1.0/tobs\n
        #Dates and Temperature Observations of most active station over the last 12 months of data\n
    
    /api/v1.0/<start>\n
        #Enter a start date in the YYYY-MM-DD format to receive the TMIN, TAVG, TMAX of data between that start date and end of data\n
    /api/v1.0/<start>/<end>\n
        #Enter a start and end date in the YYYY-MM-DD/YYYY-MM-DD (start/end respectfully) format to receive the TMIN, TAVG, TMAX of data between that start date and end of data\n
    '''

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Open Seasion
    session = Session(engine)

    # Find last date
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()

    # Calculate the date one year from the last date in data set.

    # Convert query to a string
    last_date_str = last_date[0]

    #Split string
    year, month, day = last_date_str.split("-")

    #Get date
    one_year_ago = dt.date(int(year), int(month), int(day)) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    prcp_query = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= one_year_ago).all()

    #Create List
    prcp_list = []

    for date, prcp in prcp_query:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        prcp_list.append(prcp_dict)

    #Close session
    session.close()
    
    #jsonify
    return jsonify(prcp_list)
    


@app.route("/api/v1.0/stations")
def stations():
    #Open Session
    session = Session(engine)
    
    #Query the stations table
    results = session.query(station.station, station.name)

    #Create list
    station_list = []

    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_list.append(station_dict)

    #Close Session
    session.close()

    #jsonify it
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query the last 12 months of temperature observation data

    # Open Session
    session = Session(engine)

    # Find the most active station id
    most_active_station = session.query(measurement.station, func.count(measurement.station)) \
                             .group_by(measurement.station) \
                             .order_by(func.count(measurement.station).desc()) \
                             .first()[0]

    # Starting from the most recent data point in the database. 
    last_date_temp = session.query(measurement.date).order_by(measurement.date.desc()).first()

    # Calculate the date one year from the last date in data set.

    # Convert query to a string
    last_date_temp_str = last_date_temp[0]

    #Split string
    year, month, day = last_date_temp_str.split("-")

    #Get date of one year
    one_year_ago_temp = dt.date(int(year), int(month), int(day)) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    temp_query = session.query(measurement.date, measurement.tobs).\
            filter(measurement.date >= one_year_ago_temp).\
            filter(measurement.station == most_active_station).all()

    #Create List
    tobs_list = []

    for date, tobs in temp_query:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temperature Observation"] = tobs
        tobs_list.append(tobs_dict)

    #Close Session
    session.close()

    #jsonify
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start_tobs(start):
    #Open Session
    session = Session(engine)

    #Get start date
    start_date = start #'%Y-%m-%d'
    
    # calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
    results = session.query(func.min(measurement.tobs), 
                            func.avg(measurement.tobs), 
                            func.max(measurement.tobs)).\
                filter(measurement.date >= start_date).all()
    
    # convert the query results to a dictionary
    temp_dict = {'TMIN': results[0][0], 'TAVG': results[0][1], 'TMAX': results[0][2]}
    
    #Close Session
    session.close()

    # return the JSON representation of the dictionary
    return jsonify(temp_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end_tobs(start, end):
    #Open Session
    session = Session(engine)

    # Find start and end date datetime objects
    start_date =start # '%Y-%m-%d'
    end_date = end #'%Y-%m-%d'
    
    # calculate TMIN, TAVG, and TMAX for dates between the start and end dates
    results = session.query(func.min(measurement.tobs), 
                            func.avg(measurement.tobs), 
                            func.max(measurement.tobs)).\
                filter(measurement.date >= start_date).\
                filter(measurement.date <= end_date).all()
    
    # convert the query results to a dictionary
    temp_dict = {'TMIN': results[0][0], 'TAVG': results[0][1], 'TMAX': results[0][2]}
    
    #Close session
    session.close()
    # return the JSON representation of the dictionary
    return jsonify(temp_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)