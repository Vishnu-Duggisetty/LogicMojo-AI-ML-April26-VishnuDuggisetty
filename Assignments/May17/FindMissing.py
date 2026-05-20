import pandas as pd


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


# Create employee dataset with:

# Some missing salary values
# Some missing ages

# Tasks:

# Find null values
# Count null values
# Fill missing ages using mean
# Remove rows with missing salary


employeeData = pd.read_csv("/Users/apple/Documents/LearnAI/LogicMojo-AI-ML-April26-VishnuDuggisetty/Assignments/May17/employee_missing_data.csv")
print(employeeData)
print(employeeData.isnull())  # Find null values
print(employeeData.isnull().sum())  # Count null values
employeeData.fillna({"Age": employeeData["Age"].mean()}, inplace=True)  # Fill missing ages using mean
print(employeeData)
empData = employeeData.dropna(subset=["Salary"])  # Remove rows with missing salary
print(empData)