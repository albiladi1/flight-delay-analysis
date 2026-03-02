import pandas as pd
import numpy as np
from rich import print
N= 30000
df = pd.read_csv("flights.csv",low_memory = False, nrows=N)
delayCols= ["ARRIVAL_DELAY","DEPARTURE_DELAY","AIR_SYSTEM_DELAY","SECURITY_DELAY","AIRLINE_DELAY","LATE_AIRCRAFT_DELAY","WEATHER_DELAY"]
for c in delayCols: 
    if c in df.columns:
        df[c]= pd.to_numeric(df[c], errors= "coerce")

mean = df["ARRIVAL_DELAY"].mean()
median= df["ARRIVAL_DELAY"].median()
delay= (df["ARRIVAL_DELAY"]>0).mean()*100
print("Average delay", mean)
print("Median delay", median)
print("Delay %:", delay)
print(df.groupby("AIRLINE")["ARRIVAL_DELAY"].mean().sort_values(ascending=False).head(10))
print(df.groupby("ORIGIN_AIRPORT")["ARRIVAL_DELAY"].mean().sort_values(ascending=False).head(10))
print("Average departure delay: ", df["DEPARTURE_DELAY"].mean())
print("departure delay %:", (df["DEPARTURE_DELAY"]>0).mean()*100)
correlaton= df["DEPARTURE_DELAY"].corr(df["ARRIVAL_DELAY"])
print("correlation between arrival and departure: ", correlaton)
df["DELAY_RECOVERY"]= df["ARRIVAL_DELAY"]- df["DEPARTURE_DELAY"]
print(df.groupby("AIRLINE")["DELAY_RECOVERY"].mean().sort_values(ascending= False).head(10))

