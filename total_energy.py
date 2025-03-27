import pandas as pd
import warnings

def create_total_energy_csv():

    # Suppress warnings
    warnings.filterwarnings('ignore')

    # Load the dataset
    file_path = "global_energy_consumption.csv"
    df = pd.read_csv(file_path)

    # Select only the correct columns
    selected_columns = ['Country', 'Year', 'Total Energy Consumption (TWh)']
    df_subset = df[selected_columns]
    return df_subset