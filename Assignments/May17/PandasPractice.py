import pandas as pd    ## pip install pandas
import numpy as np

# Pandas version
print(pd.__version__)

# Pandas is a powerful library for data manipulation and analysis. It provides data structures like Series and DataFrame,
# which are built on top of NumPy arrays. Pandas allows you to work with structured data, 
# perform operations like filtering, grouping, and aggregation, and handle missing data effectively. 
# It is widely used in data science and machine learning projects for data preprocessing and analysis. 
# 

data = {
    "Name": ["Vishnu", "Ram", "Anji"], 
    "Age": [25, 30, 15],
    "City": ["Hyderabad", "Delhi", "Bangalore"],
    "Salary": [50000, 60000, 30000]
}

df = pd.DataFrame(data)
print(df)
print(df.head(2))  # Display the first 2 rows of the DataFrame
print(df.tail(2))  # Display the last 2 rows of the DataFrame
print(df.info())   # Get information about the DataFrame
print(df.describe())  # Get summary statistics of the DataFrame
print(df["Age"])   # Access the "Age" column
print(df[["Name", "City"]])  # Access multiple columns
print(df[df["Age"] > 20]) # Filter rows where Age is greater than 20
print(df.groupby("Name")["Salary"].mean())  # Group by "Name" and calculate the mean salary for each city
print(df.columns)  # Get the column names of the DataFrame
print(df.index)    # Get the index of the DataFrame
print(df.values)   # Get the values of the DataFrame as a NumPy array


# Create dataset:

# Columns:

# Student
# Marks
# City

# Tasks:

# Show students with marks > 80
# Sort by marks descending
# Show only student and marks columns
# Show students from Bangalore

data = pd.read_csv("/Users/apple/Documents/LearnAI/LogicMojo-AI-ML-April26-VishnuDuggisetty/Assignments/May17/Student.csv")
df = pd.DataFrame(data)
print(df)

print(df[df["Marks"] > 80])  # Show students with marks > 80
print(df.sort_values(by="Marks", ascending=False))  # Sort by marks descending
print(df[["Student", "Marks"]])  # Show only student and marks columns
print("****************************************")
print(df[df["City"] == "Bangalore"]["Student"])  # Show students from Bangalore




## Find Missing values in a DataFrame
dataList = {"Name": ["Vishnu", "Ram", "Anji"], 
            "Age": [25, None, None],
            "City": ["Hyderabad", None, "Bangalore"],
            "Salary": [50000, 60000, None]} 

dataFrameMissing = pd.DataFrame(dataList)
print(~dataFrameMissing.isnull())  # Check for missing values in the new DataFrame with missing values
print(dataFrameMissing.isnull().sum())  # Count the number of missing values in each column of the new DataFrame with missing values
dataFrameMissingFill = dataFrameMissing.fillna({"Name" : "Your Wish", "Age": 0, "City": "My Place", "Salary": 0})
print(dataFrameMissingFill)  # Fill missing values in the new DataFrame with missing values using fillna() method
print(dataFrameMissing.dropna())  # Drop rows with missing values in the new DataFrame with missing values using dropna() method