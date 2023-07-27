import requests
from bs4 import BeautifulSoup
import statistics
import os

Base_URL = "https://books.toscrape.com/"

# Replace 'C:\Users\dell\Downloads\weddingrfp-client-data-main\weddingrfp-client-data-main\new\WebsiteScrapper\ScrapeUsingProxy' with the actual absolute path
folder_path = r'C:\Users\dell\Downloads\weddingrfp-client-data-main\weddingrfp-client-data-main\new\WebsiteScrapper\ScrapeUsingProxy'
file_path = os.path.join(folder_path, 'creds1.txt')
username, password = open(file_path, 'r').read().splitlines()

# Create a session to reuse the connection
session = requests.Session()
session.auth = (username, password)

def proxy_request(url):
    payload = {
        "source": "universal",
        "url": url,
        "geo_location": "United States"
    }

    response = session.post("https://realtime.oxylabs.io/v1/queries", json=payload)

    try:
        response_data = response.json()

        # Check if the API response contains 'results' key
        if 'results' in response_data:
            response_html = response_data['results'][0]['content']
            return BeautifulSoup(response_html, "lxml")
        else:
            print("Error: 'results' key not found in the API response.")
            print("API Response:", response_data)
    except ValueError as e:
        print(f"Error parsing API response: {e}")
        print("API Response:", response.text)

    return None

def scrape_prices(url):
    prices = []
    while url:
        soup = proxy_request(url)
        if soup is None:
            break

        price_tags = soup.find_all("p", {"class": "price_color"})
        page_prices = [float(price.string[1:]) for price in price_tags]
        prices.extend(page_prices)

        link = soup.body.find("a", string="next")
        if link:
            url = Base_URL + link['href']
        else:
            url = None

    return prices

# Starting URL for the Philosophy category
url = Base_URL + "catalogue/category/books/philosophy_7/index.html"
philosophy_prices = scrape_prices(url)

# Starting URL for the Fiction category
url = Base_URL + "catalogue/category/books/fiction_10/index.html"
fiction_prices = scrape_prices(url)

# Calculate and print statistics for both categories
print("Philosophy Prices:", philosophy_prices)
print("Mean Price (Philosophy):", statistics.mean(philosophy_prices))

print("Fiction Prices:", fiction_prices)
print("Mean Price (Fiction):", statistics.mean(fiction_prices))
