import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(0)
customer_ids = np.arange(100, 200)
ages = np.random.randint(18, 70, size=len(customer_ids))
annual_income = np.random.uniform(10000, 120000, size=len(customer_ids))
spending_score = np.random.uniform(1, 100, size=len(customer_ids))

# Create DataFrame
df = pd.DataFrame({
    'customer_id': customer_ids,
    'age': ages,
    'annual_income': annual_income,
    'spending_score': spending_score
})

# Save to CSV
df.to_csv('data/customer_data.csv', index=False)
print("Customer data CSV created.")
