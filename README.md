# WebsiteScrappingUsingPythonnandOxyLabs
This script is a web scraping script that gathers book prices from the website "https://books.toscrape.com/". It uses the BeautifulSoup library to parse the HTML content of the website and extract the prices from the relevant elements.
This script is a web scraping script that gathers book prices from the website "https://books.toscrape.com/". It uses the BeautifulSoup library to parse the HTML content of the website and extract the prices from the relevant elements.

Here's a summary of what the script does:

It imports necessary libraries, including requests for making HTTP requests, BeautifulSoup for parsing HTML, and statistics for calculating the mean price.
The script defines the base URL for the website and sets up credentials for the Oxylabs proxy service (read from a file).
A function called proxy_request(url) is defined to make a request to the Oxylabs proxy service and return a BeautifulSoup object containing the parsed HTML content.
The script then scrapes the prices for the "Philosophy" category by calling the scrape_prices(url) function. It starts from the initial URL for the "Philosophy" category and follows the "Next" links until there are no more pages to scrape. It collects all the prices into a list.
The script does the same for the "Fiction" category, scraping prices from the corresponding URL.
Finally, the script prints the collected prices for both categories and calculates and prints the mean price for each category.
If you want to upload this script to a GitHub repository, you can create a new repository on GitHub and add the script as a new file. Additionally, you might want to add a README.md file explaining what the script does and how to use it. You can also include any additional information, such as requirements, setup instructions, and usage examples in the README.

Please note that web scraping may be subject to legal considerations and the terms of service of the website you are scraping. Ensure you have the right to scrape the website's data and use the Oxylabs proxy service responsibly and in compliance with their terms and conditions.
