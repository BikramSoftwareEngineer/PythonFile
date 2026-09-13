import csv
import requests
from bs4 import BeautifulSoup

def scrape_e_commerce_products(output_file="products.csv"):
    # Target e-commerce URL
    url = "https://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        # Step 1: Send HTTP request to fetch webpage content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Step 2: Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3: Extract product information
        products = []
        for item in soup.find_all("article", class_="product_pod"):
            title = item.h3.a["title"]
            price = item.find("p", class_="price_color").get_text(strip=True)
            availability = item.find("p", class_="instock availability").get_text(strip=True)

            products.append({
                "Product Title": title,
                "Price": price,
                "Availability": availability
            })

        # Step 4: Write extracted product details into CSV file
        fieldnames = ["Product Title", "Price", "Availability"]
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)

        print(f"Success: Extracted {len(products)} products and saved to '{output_file}'.")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

if __name__ == "__main__":
    scrape_e_commerce_products()