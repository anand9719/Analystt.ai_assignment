# Python Assignment - Analystt.ai
# Part 1
# In this assignment you are required to scrape all products from this URL:
# https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2
# C283&ref=sr_pg_1
# Need to scrape atleast 20 pages of product listing pages
# Items to scrape
# • Product URL
# • Product Name
# • Product Price
# • Rating
# • Number of reviews
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

product_elements = soup.find_all('div', {'class': 's-result-item'})
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
    
    print('Product URL:', product_url)
    print('Product Name:', product_name)
    print('Product Price:', product_price)
    print('Product Rating:', product_rating)
    print('Product Reviews:', product_reviews)
    print('\n')

# Thank you Sir for giving me this opportunity, 
# Anand Agrawal