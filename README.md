# Flight Delay Analysis

This project analyzes commercial flight delay data to understand airline performance and delay patterns.

The goal of this project is to transform raw flight records into meaningful insights using data cleaning, KPI engineering, and data visualization.

## Features

- Data cleaning and preprocessing
- Calculation of key performance indicators (KPIs)
- Delay recovery analysis
- Airline performance comparison
- Interactive dashboard built with Streamlit

## Key Metrics

The analysis calculates several important metrics including:

- Average arrival delay
- Average departure delay
- Percentage of delayed flights
- Correlation between departure and arrival delays

A custom metric called **Delay Recovery** is used to measure how effectively airlines recover time during flights:


Negative values indicate successful delay recovery.

## Dataset

The dataset is not included in this repository due to GitHub file size limitations.

The analysis expects a dataset containing columns such as:

- AIRLINE
- ORIGIN_AIRPORT
- DESTINATION_AIRPORT
- SCHEDULED_DEPARTURE
- ARRIVAL_DELAY
- DEPARTURE_DELAY
- CANCELLED
- DIVERTED

## Technologies Used

1. Clone the repository

git clone https://github.com/albiladi1/flight-delay-analysis.git

2. Install required libraries

pip install pandas numpy streamlit

3. Run the analysis script

python src/analysis.py

## Project Structure

flight-delay-analysis/
│
├── src/
│   ├── analysis.py        # Data cleaning and KPI calculations
│   └── app.py             # Streamlit dashboard
│
├── README.md
└── .gitignore