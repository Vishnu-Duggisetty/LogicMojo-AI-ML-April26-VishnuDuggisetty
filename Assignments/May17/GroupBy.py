import pandas as pd

data = {
    "Department": ["HR", "IT", "Support", "Sales", "Finance"],
    "Salary": [50000, 60000, 55000, 45000, 47000]
}

df = pd.DataFrame(data)
print(df)

# Group by "Department" and calculate the mean salary for each department
result = df.groupby("Department")["Salary"].mean()
print(result)

#Count the number of employees in each department
employeeCount = df.groupby("Department").size()
print(employeeCount)




# Create sales dataset:

# Columns:

# Product
# City
# Sales

# Tasks:

# Find total sales by city
# Find average sales by product
# Find highest sales city

salesDict = {
"Nellore": {
    "Mobile": 10000,
    "Laptop": 15000,
    "Tablet": 12000,
    "Gaget": 8000,
    "Headphones": 5000
},
"Podalakur": {
    "Mobile": 8000,
    "Laptop": 12000,
    "Tablet": 10000,
    "Gaget": 6000,             
}, 
"Tirupati": {
    "Mobile": 9000,
    "Laptop": 13000,
    "Tablet": 11000,
    "Gaget": 7000,             
},
"Kavali": {
    "Laptop": 11000,
    "Tablet": 9000,
    "Gaget": 5000,             
},
"Gudur": {
    "Mobile": 6000,
    "Tablet": 8000,
    "Gaget": 4000,
}}

salesData = pd.DataFrame(salesDict)
print(salesData)
totalSales = salesData.sum()
print(totalSales)  # Find total sales by city
totalProductSales = salesData.sum(axis=1)
print(totalProductSales)
averageSales = salesData.mean(axis=1)
print(averageSales)  # Find average sales by product
highestSalesCity = salesData.sum().idxmax()
print(highestSalesCity)  # Find highest sales city
lowestSalesCity =salesData.sum().idxmin()
print(lowestSalesCity)  # Find lowest sales city