# Honolulu, Hawaii Climate Analysis
Repository for Module 10 Challenge

## Overview

This project involves a detailed climate analysis of Honolulu, Hawaii, using data collected from the region. The analysis focuses on precipitation trends and temperature observations with the goal of aiding vacation planning. The project is divided into two main parts: 

1. **Climate Analysis:** Utilizes Python, SQLAlchemy ORM queries, Pandas, and Matplotlib to explore precipitation data and station analysis.
2. **Climate App:** A Flask API based on the completed analysis, providing dynamic access to the climate data.

## Repository Structure

- `climate_starter.ipynb`: Jupyter notebook containing the climate analysis and data exploration.
- `hawaii.sqlite`: SQLite database with climate data for Honolulu.
- `app.py`: Flask application providing API access to the climate data.
- `requirements.txt`: List of Python packages required to run the notebook and app.
- `README.md`: This file, providing an overview of the project, instructions, and other documentation.

## Getting Started

### Prerequisites

- Python 3.6+
- Pip package manager

### Installation

1. Clone this repository to your local machine.

### Running the Climate Analysis

1. Open the `climate_starter.ipynb` notebook in Jupyter Notebook or JupyterLab.
2. Execute the cells in order to perform the analysis.

### Starting the Flask API

1. Navigate to the repository directory in your terminal.
2. Run the Flask application
3. Access the API through your web browser at `http://localhost:5000/`.

## Analysis Highlights

- **Precipitation Analysis:** Reveals precipitation trends over the last 12 months of data.
- **Station Analysis:** Identifies the most active weather stations and analyzes temperature trends.

## API Routes

- `/`: The homepage lists all available routes.
- `/api/v1.0/precipitation`: Returns JSON representation of the last 12 months of precipitation data.
- `/api/v1.0/stations`: Returns a JSON list of stations.
- `/api/v1.0/tobs`: Returns a JSON list of Temperature Observations (TOBS) for the previous year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Returns JSON list of the minimum, average, and maximum temperatures for a given start or start-end range.

## Conclusion

This climate analysis and data exploration provide valuable insights into the weather patterns of Honolulu, Hawaii. The associated Flask API further allows for easy access to this data, making it a valuable tool for anyone planning a trip to this beautiful destination.

## References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.

