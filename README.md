# Flight Delay Analysis

This project analyzes commercial flight delay data to better understand airline performance and delay patterns.

The goal of this project is to transform raw flight records into meaningful insights using data cleaning, KPI engineering, and data visualization.

---

## Features

- Data cleaning and preprocessing
- Calculation of key performance indicators (KPIs)
- Delay recovery analysis
- Airline performance comparison
- Interactive dashboard built with Streamlit

---

## Key Metrics

The analysis calculates several important metrics including:

- Average arrival delay
- Average departure delay
- Percentage of delayed flights
- Correlation between departure and arrival delays

A custom metric called **Delay Recovery** is used to measure how effectively airlines recover time during flights.

Delay Recovery is defined as:

Negative values indicate successful delay recovery.

---

## Dataset

The dataset used in this project is the **2015 Flight Delays and Cancellations** dataset from Kaggle.

Dataset source:
https://www.kaggle.com/datasets/usdot/flight-delays

Due to GitHub file size limitations, the dataset is not included in this repository.

After downloading the dataset, place the CSV file in the project directory before running the analysis.
## Technologies Used

- Python
- Pandas
- NumPy
- Streamlit

---

## Project Structure
flight-delay-analysis/
|
├── src/
│ └── analysis.py
│
├── README.md
└── .gitignore

---

## How to Run

1. Clone the repository
git clone https://github.com/albiladi1/flight-delay-analysis.git

2. Install required libraries
pip install pandas numpy streamlit

3. Run the analysis script
python src/analysis.py

---

## Project Goal

This project demonstrates practical data analysis skills including:

- Data preprocessing
- Feature engineering
- KPI design
- Exploratory data analysis
- Building analytical dashboards

The objective is to transform raw aviation data into actionable performance insights.
