# Python Assignment - Analystt.ai
# Part 2
# With the Product URL received in the above case, hit each URL, and add below items:
# • Description
# • ASIN
# • Product Description
# • Manufacturer
# Need to hit around 200 product URL’s and fetch various information.

import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
product_elements = soup.find_all('div', {'class': 's-result-item'})
# Create CSV file to store all information
with open('product_information.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product URL', 'Product Name', 'Product Price', 'Product Rating', 'Product Reviews', 'Product Description', 'ASIN', 'Manufacturer'])
    
    for product in product_elements:
        product_url = product.find('a', {'class': 'a-link-normal'})['href']
        product_name = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
        product_price = product.find('span', {'class': 'a-offscreen'}).text
        product_rating = product.find('div', {'class': 'a-section a-text-center'})
        if product_rating:
            product_rating = product_rating.text
        else:
            product_rating = None
        product_reviews = product.find('span', {'class': 'a-size-base'})
        if product_reviews:
            product_reviews = product_reviews.text
        else:
            product_reviews = None
        
        # Send request to URL and retrieve HTML content
        response = requests.get(product_url)
        html_content = response.content
        
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract product description and ASIN
        product_description = soup.find('div', {'class': 'a-section a-spacing-medium'}).text
        asin = soup.find('th', string='ASIN:')
        if asin:
            asin = asin.find_next_sibling().text
        else:
            asin = None
        manufacturer = soup.find('th', string='Manufacturer:')
        if manufacturer:
            manufacturer = manufacturer.find_next_sibling().text
        else:
            manufacturer = None
        # Write all information to CSV file
        writer.writerow([product_url, product_name, product_price, product_rating, product_reviews, product_description, asin

# Thank you Sir for giving me this opportunity, 
# Anand Agrawal