# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"

# Step 1: Get the HTML content
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())  # Use the prettify() method to print the formatted HTML

# Step 3: HTML Tree Traversal

# Uncomment the line to get the title of the HTML page
title = soup.title

# commonly used types of objects:
# 1. tag
# print(type(title))  # Access the title as an attribute, not a method

# 2. NavigableString
# print(type(title.string))

# 3. BeautifulSoup
# print(type(soup))

# 4. Comment

# get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)



#get the first element in the html page
print(soup.find('p')) 

# get the classes of any element in the html page
print(soup.find('p')['class']) #get the the class 

#find the all elements with the class lead
print(soup.find_all('p', class_="lead"))

# gets the text from the soup/tags
print(soup.find('p').get_text())
print(soup.get_text())


# get all the anchors tag from the page
anchors = soup.find_all('a')
all_links = []  # Fix: Initialize as a list

# get all the links on the page
for link in anchors:
    if link.get('href') and link.get('href') != '#':  # Fix: Check for valid href
        link = "https://www.codewithharry.com/" + link.get('href')
        all_links.append(link)  # Fix: Use append instead of add
        # print(link)  # Fix: Print the actual link
        
navbarSupportedContent = soup.find(id="navbarSupportedContent")

# Check if the element is found before trying to access its children
if navbarSupportedContent:
    for item in navbarSupportedContent.children:
        print(item)

print(navbarSupportedContent.next_sibling.next_sibling)
# Now you can continue with HTML tree traversal to extract the data you need.
