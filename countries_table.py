import requests
import pandas as pd

def load_dataframe():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error en la solicitud: {response.status_code}")
    
    data = response.json()
    
    df = pd.json_normalize(data)
    return df



def clean_dataframe(df):

    df_clean = pd.DataFrame({
        "name": df["name.common"],
        "population": df["population"],
        "region": df["region"],
        "area": df["area"],
    })
    
    return df_clean



def create_csv(df, path):
    df.to_csv(path, encoding="utf-8", index=False)
    return None