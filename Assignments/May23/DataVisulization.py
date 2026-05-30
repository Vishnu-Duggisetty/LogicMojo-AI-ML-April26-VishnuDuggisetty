import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px


names = ["Vishnu", "Ram", "Anji"]
salaries = [50000, 60000, 30000]

### BAR CHART
# px.bar(x=names, y=salaries, labels={"x":"Employess", "y":"Salaries"}, title="Employee Salaries").show()
plt.bar(names, salaries)
plt.xlabel("Employees")
plt.ylabel("Salaries")
plt.title("Employee Salaries")
plt.show()


#### Line Chart
salesDict = {"Nellore": 45000, "Podalakur": 35000, "Tirupati": 40000, "Kavali": 30000}
# px.line(x=list(salesDict.keys()), y=list(salesDict.values()), labels={"x": "Locations", "y": "Sales"}, title="Sales by Location").show()
plt.plot(list(salesDict.keys()), list(salesDict.values()))
plt.xlabel("Locations")
plt.ylabel("Sales")
plt.title("Sales by location")
plt.show()


## Histogram
ages = [25, 30, 15, 22, 28, 35, 40, 18, 27, 32]
plt.hist(ages)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()


## Scatter Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()