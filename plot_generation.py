import pandas as pd
import seaborn as sns
from sqlalchemy import text
import matplotlib.pyplot as plt


def generate_plots(engine):



    query = text('''SELECT
        country,
        ROUND(SUM(`Renewable_Energy_Share__%`), 2) AS total_renewable_energy,
        ROUND(SUM(`Fossil_Fuel_Dependency__%`), 2) AS total_fossil_fuel,
        ROUND(SUM(`Total_Energy_Consumption__TWh`), 2) AS total_energy_consumption
    FROM
        energy_type AS e
    WHERE
        year >= YEAR(CURRENT_DATE) - 10
    GROUP BY
        country
    ORDER BY
        total_energy_consumption DESC''')

    df = pd.read_sql(query, engine)


    # Plot 1: Renewable and fossil nergy Consumption by Country and type

    df1 = df.drop(columns=["total_energy_consumption"])

    df_melted = df1.melt(id_vars=["country"], var_name="Energy Type", value_name="Consumption")

    df_melted["Energy Type"] = df_melted["Energy Type"].replace({
        "total_renewable_energy": "Renewable",
        "total_fossil_fuel": "Fossil Fuel"
    })

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_melted, x="country", y="Consumption", hue="Energy Type", palette="muted")

    plt.xticks(rotation=45)
    plt.ylabel("Energy Consumption")
    plt.xlabel("Country")
    plt.title("Energy Consumption by Country and Type")
    plt.legend(title="Energy Type")

    plt.show()




    # Plot 2: total energy Consumption by Country and type

    df2 = df.drop(columns=["total_renewable_energy", "total_fossil_fuel"])

    df_melted = df2.melt(id_vars=["country"], var_name="Energy Type", value_name="Consumption")

    df_melted["Energy Type"] = df_melted["Energy Type"].replace({
        "total_energy_consumption": "Total energy"
    })

    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_melted, x="country", y="Consumption", hue="Energy Type", palette="muted")

    plt.xticks(rotation=45)
    plt.ylabel("Energy Consumption")
    plt.xlabel("Country")
    plt.title("Energy Consumption by Country and Type")
    plt.legend(title="Energy consumption")

    plt.show()





    # Plot 3: Evolution of Fossil Fuel Consumption in USA and Canada (2000-2024)
    query2 = text('''SELECT 
        et.Country, 
        et.Year, 
        ROUND(SUM(`Renewable_Energy_Share__%`), 2) AS Total_Renewable_Share,
        ROUND(SUM(`Fossil_Fuel_Dependency__%`), 2) AS Total_Fossil_Share,
        ROUND(SUM(`Total_Energy_Consumption__TWh`), 2) AS Total_Energy_Consumption
    FROM energy_type et
    WHERE et.Country IN ('USA', 'Canada')
    GROUP BY et.Country, et.Year
    ORDER BY et.Country, et.Year;''')

    df3 = pd.read_sql(query2, engine)



    # Filter by "Fossil_Fuel_Dependency__%" to plot fossil fuel consumption
    plt.figure(figsize=(12, 6))

    # Create the line plot
    sns.lineplot(x='Year', y='Total_Fossil_Share', hue='Country', data=df3, marker='o')

    # Customize labels and title
    plt.title('Evolution of Fossil Fuel Consumption in USA and Canada (2000-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Fossil Fuel Consumption (%)', fontsize=12)

    # Show the legend
    plt.legend(title='Country', loc='upper left')

    # Display the plot
    plt.tight_layout()
    plt.show()






    # Plot 4: Evolution of Renewable Energy Consumption in USA and Canada (2000-2024)
    
    # Filter by "Renewable_Energy_Share__%" to plot renewable energy consumption
    plt.figure(figsize=(12, 6))

    # Create the line plot
    sns.lineplot(x='Year', y='Total_Renewable_Share', hue='Country', data=df3, marker='o')

    # Customize labels and title
    plt.title('Evolution of Renewable Energy Consumption in USA and Canada (2000-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Renewable Energy Consumption (%)', fontsize=12)

    # Show the legend
    plt.legend(title='Country', loc='upper left')

    # Show the plot
    plt.tight_layout()
    plt.show()