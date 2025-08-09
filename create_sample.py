import pandas as pd

# Sample data matching your feature columns (excluding 'Class')
# You can add/change features based on your dataset columns
sample_data = {
    "V1": [0.1, -1.2, 0.5],
    "V2": [0.2, 0.3, -0.1],
    "V3": [-0.1, 1.5, 0.2],
    "V4": [0.3, -0.8, 0.6],
    "V5": [0.4, 0.0, -0.4],
    "V6": [0.1, -0.2, 0.3],
    "V7": [-0.3, 0.4, -0.1],
    "V8": [0.2, -0.1, 0.2],
    "V9": [-0.1, 0.5, -0.3],
    "V10": [0.0, -0.4, 0.1],
    "V11": [0.1, 0.2, -0.2],
    "V12": [-0.2, 0.3, 0.4],
    "V13": [0.4, -0.1, 0.0],
    "V14": [-0.3, 0.1, 0.2],
    "V15": [0.2, -0.2, 0.1],
    "V16": [0.1, 0.0, -0.1],
    "V17": [-0.1, 0.4, 0.3],
    "V18": [0.3, -0.3, 0.0],
    "V19": [0.0, 0.1, -0.2],
    "V20": [-0.2, 0.0, 0.2],
    "V21": [0.1, -0.1, 0.0],
    "V22": [0.0, 0.3, -0.1],
    "V23": [-0.3, 0.2, 0.4],
    "V24": [0.2, -0.4, 0.1],
    "V25": [0.1, 0.0, -0.3],
    "V26": [-0.1, 0.1, 0.2],
    "V27": [0.3, -0.2, 0.0],
    "V28": [0.0, 0.4, -0.1],
    "Amount": [100.0, 250.5, 30.75]
}

df_sample = pd.DataFrame(sample_data)

# Save as CSV
df_sample.to_csv("sample_transactions.csv", index=False)
print("Sample CSV file 'sample_transactions.csv' created!")
