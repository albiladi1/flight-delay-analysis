import pandas as pd
import numpy as np
delay_cols= ["ARRIVAL_DELAY",
    "DEPARTURE_DELAY",
    "AIR_SYSTEM_DELAY",
    "SECURITY_DELAY",
    "AIRLINE_DELAY",
    "LATE_AIRCRAFT_DELAY",
    "WEATHER_DELAY",]
needed_cols= ["AIRLINE",
    "ORIGIN_AIRPORT",
    "DESTINATION_AIRPORT",
    "SCHEDULED_DEPARTURE",
    "ARRIVAL_DELAY",
    "DEPARTURE_DELAY",
    "CANCELLED",
    "DIVERTED",]
def load_data (csv_path: str, nrows: int| None= None)-> pd.DataFrame:
    df= pd.read_csv(csv_path, low_memory=False , nrows= nrows)

    missing= [c for c  in needed_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    for c in ["CANCELLED", "DIVERTED"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

    df["IS_CANCELLED"]=df["CANCELLED"].eq(1)
    df["IS_DIVERTED"]= df["DIVERTED"].eq(1)
    df= df.loc[~df["IS_CANCELLED"]].copy()
    df = df.loc[~df["IS_DIVERTED"]].copy()

    df= df.dropna(
        subset= ["AIRLINE",
            "ORIGIN_AIRPORT",
            "DESTINATION_AIRPORT",
            "SCHEDULED_DEPARTURE",
            "ARRIVAL_DELAY",
            "DEPARTURE_DELAY",
            ]
    )

    df["SCHEDULED_DEPARTURE"]= pd.to_numeric(df["SCHEDULED_DEPARTURE"], errors="coerce")
    df = df.dropna(subset=["SCHEDULED_DEPARTURE"])
    df["SCHEDULED_DEPARTURE"]= df["SCHEDULED_DEPARTURE"].astype(int)
    df["IS_DELAYED_ARR"] = df["ARRIVAL_DELAY"] > 0
    df["IS_DELAYED_DEP"] = df["DEPARTURE_DELAY"] > 0
    df_recovery = df[df["DEPARTURE_DELAY"] > 0].copy()

    df_recovery["DELAY_RECOVERY"] = (
    df_recovery["ARRIVAL_DELAY"] - df_recovery["DEPARTURE_DELAY"] 
    )
    return df, df_recovery
def quick_kpis(df:pd.DataFrame)-> dict:
    kpis={
        "rows": len(df),
         "avg_arrival_delay" : float(df[ "ARRIVAL_DELAY"].mean()),
         "avg_departure_delay": float(df["DEPARTURE_DELAY"].mean()),
         "pct_arrival_delayed": float(df["IS_DELAYED_ARR"].mean() * 100),
        "pct_departure_delayed": float(df["IS_DELAYED_DEP"].mean() * 100),
        "corr_arr_dep": float(df["ARRIVAL_DELAY"].corr(df["DEPARTURE_DELAY"])),
    }
    return kpis

if __name__== "__main__": 
    df, df_recovery = load_data("flights.csv", nrows=30000)
    kpis= quick_kpis(df)
    print("Rows", kpis["rows"])
    print("Avg arrival delay:", kpis["avg_arrival_delay"])
    print("avg departure delay:", kpis["avg_departure_delay"])
    print("avg arrival delayed %", kpis["pct_arrival_delayed"])
    print("avg departure delayed %", kpis["pct_departure_delayed"])
    print("Corr(arrival vs departure):", kpis["corr_arr_dep"])

    print("\n Top 10 airlines by best DELAY_RECOVERY (most negative= best recovery):")
    print(df_recovery.groupby("AIRLINE")["DELAY_RECOVERY"].mean().sort_values().head(10))

    

