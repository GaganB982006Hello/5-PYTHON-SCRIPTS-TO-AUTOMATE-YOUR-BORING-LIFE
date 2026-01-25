import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    url = "https://example.com/products" # Replace with target website
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the specific table or data containers
        products = []
        for item in soup.find_all('div', class_='product-item'):
            name = item.find('h2', class_='title').text.strip()
            price = item.find('span', class_='price').text.strip()
            products.append({"Name": name, "Price": price})
        
        # Convert to DataFrame and save to Excel
        df = pd.DataFrame(products)
        df.to_excel("Market_Data.xlsx", index=False)
        print("Data scraped and saved to Market_Data.xlsx")
    else:
        print("Failed to retrieve website.")

if __name__ == "__main__":
    scrape_data()
