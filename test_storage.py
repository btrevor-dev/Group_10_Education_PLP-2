#!/usr/bin/env python3
from storage import load_data, save_data

# Load current data
data = load_data()

# Add test data
data["sample_user"] = {"score": 100}

# Save data
save_data(data)

# Load again and print to verify
print("Current Data:", load_data())
