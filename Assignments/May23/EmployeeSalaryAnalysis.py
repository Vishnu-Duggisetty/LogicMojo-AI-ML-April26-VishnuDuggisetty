import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
# Clean data
# Find average salary
# Find highest paid department
# Create charts
# Create heatmap
# Find correlations

employeeData = pd.read_csv("/Users/apple/Documents/LearnAI/LogicMojo-AI-ML-April26-VishnuDuggisetty/Assignments/May17/employee_missing_data.csv")
print(employeeData)

nameNa = employeeData.dropna(subset=["Name"])
print(nameNa)
employeeData["Department"] = employeeData["Department"].fillna("Recommendations")
print(employeeData)
employeeData["Salary"] = employeeData["Salary"].fillna(employeeData["Salary"].mean())
print(employeeData)
employeeData = employeeData.fillna({"Age": 25, "Experience": 2, "City": "Nellore", "Name": "Your Wish"})
print(employeeData)
avergaeSalary = employeeData["Salary"].mean()
print("Average Salary:", avergaeSalary)
groupByDepartment = employeeData.groupby("Department")["Salary"].sum()
print(groupByDepartment)
highestPaidDepart = groupByDepartment.idxmax()
print("Highest Paid Department:", highestPaidDepart)
plt.bar(groupByDepartment.index, groupByDepartment.values)
plt.xlabel("Department")
plt.ylabel("Total Salary")
plt.title("Salary Distribution by Department")
plt.show()

plt.pie(groupByDepartment.values, labels=groupByDepartment.index, autopct="%1.1f%%")
plt.title("Salary Distribution by Department")
plt.show()

emplCorr = employeeData[["Age", "Experience", "Salary"]].corr()
print(emplCorr)
sns.heatmap(emplCorr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()



## add current Lpa 
employeeData["Current_LPA"] = (employeeData["Salary"] * 12) / 100000
print(employeeData)

hrPolicySalarayData = pd.read_csv("/Users/apple/Documents/LearnAI/LogicMojo-AI-ML-April26-VishnuDuggisetty/Assignments/May23/HrPolicySalaryTable.csv")
print(hrPolicySalarayData)


def experenceBrand(exp): 
    if exp >= 1 and exp <= 2:
        return "1-2 yrs"
    if exp > 2 and exp <= 5:
        return "2-5 yrs"
    if exp > 5 and exp <= 10:
        return "5-10 yrs"
    return "10+ yrs"

employeeData["EXP_BRAND"] = employeeData["Experience"].apply(experenceBrand)
print(employeeData)


mergedDf = pd.merge(employeeData, hrPolicySalarayData, left_on=["Department", "EXP_BRAND"], right_on=["Department", "Experience"], how="left")
print(mergedDf)

mergedDf[["Min_LPA", "Max_LPA"]] = mergedDf["Salary Range"].str.replace("L", "").str.split("-", expand=True).astype(float)
print(mergedDf)


def salaryStatus(row):
    currentLpa = row["Current_LPA"]
    minLpa = row["Min_LPA"]
    maxLpa = row["Max_LPA"]

    if currentLpa < minLpa: 
        return "Underpaid"
    elif currentLpa > maxLpa:
        return "Overpaid"
    
    return "Correctly Paid"

mergedDf["Salary_Status"] = mergedDf.apply(salaryStatus, axis=1)
salaryStatusTable = mergedDf[["Name", "Department", "EXP_BRAND", "Current_LPA", "Salary Range", "Salary_Status"]]
print(salaryStatusTable)


sns.barplot(x="Name", y="Current_LPA", hue="Salary_Status", data=mergedDf)
plt.xlabel("Employees")
plt.ylabel("Current LPA")
plt.title("Employee Salary Status")
plt.xticks(rotation=45)
plt.show()

plt.pie(mergedDf["Salary_Status"].value_counts(), labels=mergedDf["Salary_Status"].value_counts().index, autopct="%1.1f%%")
plt.title("Salary Status Distribution")
plt.show()

sns.countplot(x="Salary_Status", data=mergedDf)
plt.xlabel("Salary Status")
plt.ylabel("Count")
plt.title("Count of Salary Status")
plt.show()