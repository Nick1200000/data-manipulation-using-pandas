import numpy as np
import pandas as pd
import json
import requests
# Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'Tokyo'],
    'Salary': [50000, 54000, 48000, 60000, 58000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
