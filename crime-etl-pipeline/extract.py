import pandas as pd

def extract():
    df = pd.read_csv("/Users/bri/Downloads/crimes-in-seattle/SPD_Crime_Data__2008-Present_20260317.csv")
    print("Data extracted")
    return df