#   Honolulu, Hawaii Climate Analysis

## Introduction

Welcome to the Honolulu, Hawaii climate analysis project! If you're planning a vacation in this beautiful destination, you've come to the right place. In this project, I've conducted a thorough climate analysis of Honolulu, Hawaii, using Python, SQLAlchemy, Pandas, and Matplotlib. The analysis provides valuable insights into the weather patterns in the area, helping you plan your trip more effectively.

## Part 1: Analyze and Explore the Climate Data

In this section, I've performed a comprehensive climate analysis and data exploration using the provided files (`climate_starter.ipynb` and `hawaii.sqlite`). Here are the key steps:

1.  **Database Connection:** I connected to the SQLite database using SQLAlchemy's `create_engine()` function.
    
2.  **Data Reflection:** The tables were reflected into classes using SQLAlchemy's `automap_base()` function, and references to the `station` and `measurement` classes were saved for data analysis.
    
3.  **SQLAlchemy Session:** A SQLAlchemy session was created to link Python to the database. It's important to note that the session was closed at the end of the notebook to ensure proper resource management.
    

### Precipitation Analysis

1.  **Most Recent Date:** I found the most recent date in the dataset.
    
2.  **12 Months of Precipitation Data:** Using the most recent date, I retrieved the previous 12 months of precipitation data by querying the database.
    
3.  **Data Visualization:** The results were loaded into a Pandas DataFrame, sorted by date, and then plotted as a line graph to visualize precipitation trends.
    
4.  **Summary Statistics:** Pandas was used to calculate and print the summary statistics for the precipitation data.
    

### Station Analysis

1.  **Total Stations:** I designed a query to calculate the total number of stations in the dataset.
    
2.  **Most Active Stations:** I identified the most active stations by listing them in descending order based on observation counts.
    
3.  **Temperature Analysis:** For the most active station, I calculated the lowest, highest, and average temperatures.
    
4.  **Temperature Observation (TOBS) Data:** I obtained the previous 12 months of temperature observation (TOBS) data for the most active station and visualized it as a histogram.
    

## Part 2: Design Your Climate App

In this section, I've designed a Flask API based on the analysis conducted. The following routes have been created:

1.  **Homepage `/`:** Provides a list of all available routes.
    
2.  **Precipitation Data `/api/v1.0/precipitation`:** Returns the last 12 months of precipitation data in JSON format.
    
3.  **Stations `/api/v1.0/stations`:** Returns a list of stations in JSON format.
    
4.  **Temperature Observations `/api/v1.0/tobs`:** Returns the previous year's temperature observations for the most active station in JSON format.
    
5.  **Temperature Statistics `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`:** Returns JSON data for minimum, average, and maximum temperatures based on user-defined start and end dates.
    

This climate analysis and API design will be invaluable for planning your vacation in Honolulu, Hawaii. Enjoy your trip!

### References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910,  [https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.](https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)
