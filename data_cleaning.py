# =========================================================
# STEP 2 : DATA CLEANING
# =========================================================

import pandas as pd

# Load dataset
df = pd.read_csv("raw_dynamic_pricing_data.csv")

print("\nRAW DATA\n")
print(df.head())

# ---------------------------------------------------------
# CLEAN REVIEWS
# ---------------------------------------------------------

df["Reviews"] = df["Reviews"].str.extract(r'(\d+)')

df["Reviews"] = df["Reviews"].astype(int)

# ---------------------------------------------------------
# REMOVE DUPLICATES
# ---------------------------------------------------------

df.drop_duplicates(inplace=True)

# ---------------------------------------------------------
# CHECK NULL VALUES
# ---------------------------------------------------------

print("\nMISSING VALUES\n")
print(df.isnull().sum())

# ---------------------------------------------------------
# SAVE CLEANED DATA
# ---------------------------------------------------------

df.to_csv(
    "cleaned_dynamic_pricing_data.csv",
    index=False
)

print("\nData Cleaning Completed Successfully")