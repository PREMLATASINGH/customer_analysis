import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Number of rows
n = 1000

# Customer Segments
segments = ["Bronze", "Silver", "Gold", "Platinum"]

# Cities
cities = ["New York", "Chicago", "Houston", "San Francisco", "Los Angeles",
          "Boston", "Seattle", "Miami", "Dallas", "Atlanta"]

# Generate dataset
data = {
    "CustomerID": [fake.unique.random_int(min=1000, max=9999) for _ in range(n)],
    "Name": [fake.name() for _ in range(n)],
    "Age": np.random.randint(18, 70, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "City": np.random.choice(cities, n),
    "JoinDate": [fake.date_between(start_date='-5y', end_date='today') for _ in range(n)],
    "LastPurchaseDate": [fake.date_between(start_date='-1y', end_date='today') for _ in range(n)],
    "TotalOrders": np.random.randint(1, 50, n),
    "PurchaseAmount": np.round(np.random.uniform(20, 2000, n), 2),
    "CustomerSegment": np.random.choice(segments, n),
    "Churn": np.random.choice([0, 1], n, p=[0.8, 0.2])  # 20% churn rate
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("customer_analysis_1000.csv", index=False)

print("customer_analysis_1000.csv created successfully!")
df = pd.read_csv("customer_analysis_1000.csv")
print(df.head())
df.head()
df.info()
df.describe()
print(df.nlargest(10, "PurchaseAmount"))
print(df.groupby("CustomerSegment")["PurchaseAmount"].mean())
