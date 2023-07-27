import requests
from bs4 import BeautifulSoup
import statistics
import os

Base_URL = "https://books.toscrape.com/"
url = Base_URL + "catalogue/category/books/philosophy_7/index.html"

# Replace 'C:\Users\dell\Downloads\weddingrfp-client-data-main\weddingrfp-client-data-main\new\WebsiteScrapper\ScrapeUsingProxy' with the actual absolute path
folder_path = r'C:\Users\dell\Downloads\weddingrfp-client-data-main\weddingrfp-client-data-main\new\WebsiteScrapper\ScrapeUsingProxy'
file_path = os.path.join(folder_path, 'creds1.txt')
username, password = open(file_path, 'r').read().splitlines()


def proxy_request(url):
    payload = {
        "source": "universal",
        "url": url,
        "geo_location": "United States"
    }
    response = requests.request(
        "POST", "https://realtime.oxylabs.io/v1/queries",
        auth=(username, password),
        json=payload
    )

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

soup = proxy_request(url)

if soup is not None:
    price_tags = soup.find_all("p", {"class": "price_color"})
    prices = [float(price.text[2:]) for price in price_tags]
    print(prices)
    print(statistics.mean(prices))
#https://books.toscrape.com/catalogue/category/books/fiction_10/page-1.html
cat="/catalogue/category/books/fiction_10/"
url=Base_URL +cat + "index.html"
prices=[]
next_link=True
while next_link:
    soup=proxy_request(url)
    price_tags = soup.find_all("p", {"class": "price_color"})
    page_prices = [float(price.string[1:]) for price in price_tags]
    # for page_price in page_prices:
    prices +=page_prices
    link=soup.body.find("a",string="next")
    if link:
        url=Base_URL +cat +link['href']
    else:
        next_link=False
print(prices)
print(statistics.mean(prices))
