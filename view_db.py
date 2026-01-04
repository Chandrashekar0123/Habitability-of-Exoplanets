import sqlite3
import pandas as pd

conn = sqlite3.connect("exoplanets.db")

df = pd.read_sql_query("SELECT * FROM predictions", conn)
print(df)

# Save to CSV
df.to_csv("predictions.csv", index=False)

conn.close()
