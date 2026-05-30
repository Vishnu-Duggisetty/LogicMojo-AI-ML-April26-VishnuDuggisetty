import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create charts for:

# Student marks
# Monthly expenses
# Daily temperature
# Employee salaries

studentData = pd.read_csv("/Users/apple/Documents/LearnAI/LogicMojo-AI-ML-April26-VishnuDuggisetty/Assignments/May17/Student.csv")
print(studentData)
plt.bar(studentData["Student"], studentData["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

monthlyExpenses = {
    "Rent": 15000,
    "Groceries": 5000,
    "Utilities": 3000,
    "Entertainment": 2000,
    "Transportation": 4000
}

plt.pie(monthlyExpenses.values(), labels=monthlyExpenses.keys(), autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.show()

dailyTemperature = {
    "Monday": 30,
    "Tuesday": 32,
    "Wednesday": 28,
    "Thursday": 31,
    "Friday": 29,
    "Saturday": 27,
    "Sunday": 26
}
plt.plot(list(dailyTemperature.keys()), list(dailyTemperature.values()))
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature")
plt.show()

employeeSalaries = {
    "Vishnu": 50000,
    "Ram": 60000,
    "Anji": 30000,
    "Sita": 55000,
    "Gita": 45000
}
plt.bar(employeeSalaries.keys(), employeeSalaries.values())
plt.xlabel("Employees")
plt.ylabel("Salaries")
plt.title("Employee Salaries")
plt.show()


