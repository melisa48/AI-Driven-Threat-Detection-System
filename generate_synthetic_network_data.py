import numpy as np
import pandas as pd

# Parameters for synthetic data generation
n_samples = 1000
n_features = 20

# Generating normal traffic data
normal_data = np.random.normal(loc=0, scale=1, size=(n_samples, n_features))

# Generating abnormal traffic data
abnormal_data = np.random.normal(loc=5, scale=1.5, size=(int(n_samples * 0.1), n_features))

# Combine and label the data
data = np.vstack((normal_data, abnormal_data))
labels = np.hstack((np.zeros(n_samples), np.ones(int(n_samples * 0.1))))

# Convert to DataFrame
df = pd.DataFrame(data)
df['label'] = labels

# Save to CSV (optional)
df.to_csv('synthetic_network_data.csv', index=False)

print(df.head())
