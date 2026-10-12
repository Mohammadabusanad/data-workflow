"""
Product Inventory Analyzer
Fetches product data from an API, filters in-stock items,
calculates total inventory value, and saves results to JSON.
"""

import requests
import json

try:
    # Fetch data from the API
    response = requests.get("https://api.example.com/Products")
    response.raise_for_status()
    products = response.json()

    # Filter available products and calculate total value
    products_result = []
    total_products = 0
    available_products = 0
    total_inventory_value = 0

    for product in products:
        total_products += 1

        if product["stock"] > 0:
            available_products += 1

            item = {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "total_value": product["price"] * product["stock"]
            }

            products_result.append(item)
            total_inventory_value += product["price"] * product["stock"]

    # Save results to JSON file
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products_result, file, indent=4)

    print("Total products:", total_products)
    print("Available products:", available_products)
    print("Total inventory value:", total_inventory_value)
    print("File saved successfully.")

except requests.exceptions.HTTPError:
    print("Request failed")