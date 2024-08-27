import pandas as pd
from sklearn.cluster import KMeans
import joblib

# Load the cleaned data
data = pd.read_csv('data/cleaned_customer_data.csv')

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=0)
data['cluster'] = kmeans.fit_predict(data[['age', 'annual_income', 'spending_score']])

# Save the model and the clustered data
joblib.dump(kmeans, 'models/kmeans_model.pkl')
data.to_csv('data/segmented_customer_data.csv', index=False)
