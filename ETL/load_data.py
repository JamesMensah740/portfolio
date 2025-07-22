import pandas as pd
import sqlite3

# Load your dataset
df = pd.read_csv("data/employee_attrition.csv")

# Save to SQLite
conn = sqlite3.connect("data/employee_data.db")
df.to_sql("employee_attrition", conn, if_exists="replace", index=False)
conn.close()

print("✅ Data loaded into SQLite successfully.")
