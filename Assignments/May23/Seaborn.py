import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


dailyExpenses = {
    "Salary": ["50000", "60000", "55000", "45000", "47000"], 
    "Expenses": ["20000", "15000", "18000", "22000", "17000"], 
    "Savings": ["30000", "45000", "37000", "23000", "30000"]
    }

df = pd.DataFrame(dailyExpenses)
print(df)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()