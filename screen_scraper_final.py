# File name: screen_scraper.py
# Author: Johnny Mendoza
# Date created: 12/27/2017
# Date last modified: 1/29/2017
# Python Version: 2.7
# Description: This program will scrape product data from a website
# brand, product name and shipping, and then format it and
# save it to a CSV file that can be opened in Microsoft Excel

# import beautiful soup 4 and use urllib to import urlopen
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# url where we will grab the product data
my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# open connection and grab the URL page information, read it, then close it
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parse html from the page
page_soup = soup(page_html, "html.parser")

# find each product within the item-container class
containers = page_soup.findAll("div",{"class":"item-container"})

# write a file named products.csv with the data returned
filename = "products.csv"
f = open(filename, "w")

# create headers for products
headers = "price, product_name, shipping\n"

# writes text to the file
f.write("")

# define containers based on location on webpage and their DOM elements
for container in containers:
    price_container = container.findAll("li", {"class":"price-current"})
    price = price_container[0].text.strip("|")

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

# print each product with the brand, product name and shipping cost
print("price: " + price)
print("product name: " + product_name)
print("shipping: " + shipping)

# when writing each section, add a comma, replace comma with pipe,
# add new line after shipping
f.write(price + "," + product_name.replace(",", "|") + "," + shipping + "\n")

# close the f.write with f.close
f.close()
