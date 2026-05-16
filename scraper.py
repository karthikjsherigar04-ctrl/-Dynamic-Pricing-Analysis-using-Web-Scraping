# =========================================================
# STEP 1 : WEB SCRAPING
# =========================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

# Website URL
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("div", class_="thumbnail")

# Empty list
data = []

# Loop through products
for product in products:

    # Product Name
    name_tag = product.find("a", class_="title")
    name = name_tag.text.strip() if name_tag else "No Name"

    # Selling Price
    price_tag = product.find("h4", class_="price")
    selling_price = price_tag.text.strip() if price_tag else "$0"

    # Reviews
    review_tag = product.find("p", class_="review-count")

    if review_tag:
        reviews = review_tag.text.strip()
    else:
        reviews = "0 reviews"

    # Ratings
    rating_div = product.find("div", class_="ratings")

    if rating_div:
        rating = len(rating_div.find_all("span"))
    else:
        rating = 0

    # -----------------------------------------------------
    # GENERATE ORIGINAL PRICE
    # -----------------------------------------------------

    numeric_price = float(
        selling_price.replace("$", "")
    )

    # Original price higher than selling price
    original_price = numeric_price + random.randint(50, 300)

    # Store data
    data.append([
        name,
        original_price,
        numeric_price,
        reviews,
        rating
    ])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "Product_Name",
        "Original_Price",
        "Selling_Price",
        "Reviews",
        "Rating"
    ]
)

# Save raw dataset
df.to_csv("raw_dynamic_pricing_data.csv", index=False)

print(df.head())

print("\nWeb Scraping Completed Successfully")