# =========================================================
# STEP 3 : DYNAMIC PRICING ANALYSIS + EDA
# =========================================================

import pandas as pd

# Load dataset
df = pd.read_csv(
    "cleaned_dynamic_pricing_data.csv"
)

# ---------------------------------------------------------
# DISCOUNT PERCENTAGE
# ---------------------------------------------------------

df["Discount_Percentage"] = (
    (
        df["Original_Price"]
        - df["Selling_Price"]
    )
    / df["Original_Price"]
) * 100

# ---------------------------------------------------------
# DISPLAY DATA
# ---------------------------------------------------------

print("\nDYNAMIC PRICING DATA\n")

print(df.head())

# ---------------------------------------------------------
# AVERAGE DISCOUNT
# ---------------------------------------------------------

avg_discount = df[
    "Discount_Percentage"
].mean()

print("\nAverage Discount Percentage:")
print(round(avg_discount, 2), "%")

# ---------------------------------------------------------
# HIGHEST DISCOUNT PRODUCT
# ---------------------------------------------------------

highest_discount = df.sort_values(
    by="Discount_Percentage",
    ascending=False
)

print("\nHighest Discount Product:")

print(
    highest_discount[
        [
            "Product_Name",
            "Discount_Percentage"
        ]
    ].head(1)
)

# ---------------------------------------------------------
# MOST EXPENSIVE PRODUCT
# ---------------------------------------------------------

most_expensive = df.sort_values(
    by="Selling_Price",
    ascending=False
)

print("\nMost Expensive Product:")

print(
    most_expensive[
        [
            "Product_Name",
            "Selling_Price"
        ]
    ].head(1)
)

# ---------------------------------------------------------
# MOST REVIEWED PRODUCT
# ---------------------------------------------------------

most_reviewed = df.sort_values(
    by="Reviews",
    ascending=False
)

print("\nMost Reviewed Product:")

print(
    most_reviewed[
        [
            "Product_Name",
            "Reviews"
        ]
    ].head(1)
)

# Save updated dataset
df.to_csv(
    "dynamic_pricing_analysis.csv",
    index=False
)

print("\nDynamic Pricing Analysis Completed")