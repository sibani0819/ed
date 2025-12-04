import pandas as pd
import matplotlib.pyplot as plt

# 1. Load employee data from CSV
# Replace the filename with your actual file name
df = pd.read_csv("employee_data.csv")

# 2. Count how many employees are in the "Sales" department
sales_count = df[df["Department"] == "Sales"].shape[0]

# 3. Print that count
print("Number of employees in Sales department:", sales_count)

# 4. Make a histogram (bar chart) of all departments
dept_counts = df["Department"].value_counts()

plt.figure(figsize=(8, 5))
dept_counts.plot(kind="bar")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
