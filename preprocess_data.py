import pandas as pd

# Load the customer data
data = pd.read_csv('data/customer_data.csv')

# Example preprocessing: Fill missing values forward
# Old method
# data.fillna(method='ffill', inplace=True)

# Updated method to avoid the warning
data.ffill(inplace=True)

# Additional preprocessing steps...

# Save the cleaned data
data.to_csv('data/cleaned_customer_data.csv', index=False)
