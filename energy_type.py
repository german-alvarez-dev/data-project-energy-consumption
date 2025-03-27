import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def load_csv():
    df = pd.read_csv("global_energy_consumption.csv")

    df_filtered = df[['Country', 'Year', 'Renewable Energy Share (%)', 'Fossil Fuel Dependency (%)', 'Total Energy Consumption (TWh)']]

    df_filtered.columns = df_filtered.columns.str.replace(' ', '_').str.replace('(', '_').str.replace(')', '')

    return df_filtered
