SELECT
    country,
    ROUND(SUM(`Renewable_Energy_Share__%`), 2) AS total_renewable_energy,
    ROUND(SUM(`Fossil_Fuel_Dependency__%`), 2) AS total_fossil_fuel,
    ROUND(SUM(Total_Energy_Consumption__TWh), 2) AS total_energy_consumption
FROM
    energy_type AS e
WHERE
    year >= YEAR(CURRENT_DATE) - 10
GROUP BY
    country
ORDER BY
    total_energy_consumption DESC;
    
    
    
SELECT 
    et.Country, 
    et.Year, 
    ROUND(SUM(`Renewable_Energy_Share__%`), 2) AS Total_Renewable_Share,
    ROUND(SUM(`Fossil_Fuel_Dependency__%`), 2) AS Total_Fossil_Share,
    ROUND(SUM(`Total_Energy_Consumption__TWh`), 2) AS Total_Energy_Consumption
FROM energy_type et
WHERE et.Country IN ('USA', 'Canada')
GROUP BY et.Country, et.Year
ORDER BY et.Country, et.Year;