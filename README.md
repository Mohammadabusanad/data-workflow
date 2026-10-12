# Product Inventory Analyzer

A Python automation script that fetches product data from a remote API,
processes it, and exports structured results to a JSON file.

## What It Does
- Fetches product data from an external API
- Filters products and keeps only items in stock
- Calculates total inventory value for each product
- Generates summary statistics (total products, available products, total value)
- Exports the processed results to a products.json file

## How to Run
1. Install the required library:
pip install requests

2. Update the API URL in the script with your own endpoint

3. Run:
python dataWorkflow.py

## Note
The included API URL is a placeholder. In a real scenario, the script
connects to a live endpoint (with authentication if required) and pulls
data automatically.

## Technologies
- Python
- requests
- json