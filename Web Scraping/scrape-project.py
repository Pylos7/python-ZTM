import requests
from bs4 import BeautifulSoup
import pprint

# Get page response from request
res = requests.get('https://www.namebadgers.com/shop/name-badges')
res2 = requests.get('https://www.namebadgers.com/shop/name-badges?sort=&page=2&limit=16')

# Converts a string into something we can actually use
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')


# Using CSS Selectors to make links and prices lists
links = soup.select('.prdocutname') # Class with the product link we want
prices = soup.select('.oneprice') # Class with the price info
links2 = soup2.select('.prdocutname') # Class with the product link we want
prices2 = soup2.select('.oneprice') # Class with the price info

mega_links = links + links2
mega_prices = prices + prices2

def sort_items_by_price(nblist):
    return sorted(nblist, key= lambda k:k['Price'])

def create_custom_nb(links, prices):
    nb = []
    for idx, item in enumerate(links):
        # Title and Links
        title = item.getText().replace('\t\t\t\t\t\t\t()','') # Remove tabs from title
        href = item.get('href', None)
        # Prices
        cost = float(prices[idx].getText().replace('$', ''))
        # Dictionary
        nb.append({'Title': title, 'Link': href, 'Price': cost})
    return sort_items_by_price(nb)

pprint.pprint(create_custom_nb(mega_links, mega_prices))
