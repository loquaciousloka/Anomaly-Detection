import pandas as pd
import sqlite3
# Connect to the database
conn = sqlite3.connect('transactionsdb.db')

# Retrieve data from 'transactions' table
query = "SELECT * FROM transactions"
df = pd.read_sql_query(query, conn)

# Find transactions with negative or unusually high amounts
anomalous_amounts = df[(df['transaction_amount'] < 0) | (df['transaction_amount'] > 10000)]
print("Anomalous transactions by amount:")
print(anomalous_amounts)

# Find missing customer information
missing_info = df[df['customer_id'].isnull() | df['customer_name'].isnull()]
print("\nTransactions with missing customer information:")
print(missing_info)

# Find transactions that occurred outside business hours (9-5)
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
outside_business_hours = df[(df['transaction_date'].dt.hour < 9) | (df['transaction_date'].dt.hour >= 17)]
print("\nTransactions outside business hours:")
print(outside_business_hours)

# Close the database connection
conn.close()
