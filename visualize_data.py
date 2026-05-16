# =========================================================
# STEP 4 : ADVANCED DATA VISUALIZATION
# =========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dynamic_pricing_analysis.csv")

# ---------------------------------------------------------
# STYLE SETTINGS
# ---------------------------------------------------------

sns.set_style("darkgrid")

plt.rcParams["figure.figsize"] = (10, 5)

# =========================================================
# 1. DISCOUNT PERCENTAGE DISTRIBUTION
# =========================================================

plt.figure()

sns.histplot(
    df["Discount_Percentage"],
    bins=6,
    kde=True
)

plt.title(
    "Distribution of Discount Percentage",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Discount Percentage")

plt.ylabel("Number of Products")

plt.tight_layout()

plt.show()

# =========================================================
# 2. ORIGINAL PRICE VS SELLING PRICE
# =========================================================

top_products = df.head(5)

x = range(len(top_products))

width = 0.35

plt.figure(figsize=(12,6))

plt.bar(
    [i - width/2 for i in x],
    top_products["Original_Price"],
    width=width,
    label="Original Price"
)

plt.bar(
    [i + width/2 for i in x],
    top_products["Selling_Price"],
    width=width,
    label="Selling Price"
)

plt.xticks(
    x,
    top_products["Product_Name"],
    rotation=15
)

plt.title(
    "Original Price vs Selling Price",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Products")

plt.ylabel("Price")

plt.legend()

plt.tight_layout()

plt.show()

# =========================================================
# 3. SELLING PRICE VS REVIEWS
# =========================================================

plt.figure()

sns.scatterplot(
    x="Selling_Price",
    y="Reviews",
    size="Rating",
    data=df,
    sizes=(100, 400)
)

plt.title(
    "Selling Price vs Reviews",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Selling Price")

plt.ylabel("Reviews")

plt.tight_layout()

plt.show()

# =========================================================
# 4. TOP DISCOUNT PRODUCTS
# =========================================================

top_discount = df.sort_values(
    by="Discount_Percentage",
    ascending=False
).head(5)

plt.figure(figsize=(12,6))

sns.barplot(
    x="Discount_Percentage",
    y="Product_Name",
    data=top_discount,
    palette="viridis"
)

plt.title(
    "Top Discounted Products",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Discount Percentage")

plt.ylabel("Product Name")

plt.tight_layout()

plt.show()

# =========================================================
# 5. PRODUCT RATINGS DISTRIBUTION
# =========================================================

plt.figure()

sns.countplot(
    x="Rating",
    data=df,
    palette="magma"
)

plt.title(
    "Ratings Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Ratings")

plt.ylabel("Count")

plt.tight_layout()

plt.show()


# =========================================================
# 6. CORRELATION HEATMAP
# =========================================================

plt.figure(figsize=(8,6))

correlation = df[
    [
        "Original_Price",
        "Selling_Price",
        "Reviews",
        "Rating",
        "Discount_Percentage"
    ]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Correlation Heatmap",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

plt.show()

# =========================================================
# 7. TOP REVIEWED PRODUCTS
# =========================================================

top_reviewed = df.sort_values(
    by="Reviews",
    ascending=False
).head(5)

plt.figure(figsize=(12,6))

sns.barplot(
    x="Reviews",
    y="Product_Name",
    data=top_reviewed,
    palette="coolwarm"
)

plt.title(
    "Top Reviewed Products",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Number of Reviews")

plt.ylabel("Product Name")

plt.tight_layout()

plt.show()

# =========================================================
# FINAL MESSAGE
# =========================================================

print("\nAdvanced Visualization Completed Successfully")