from bs4 import BeautifulSoup
import requests

# Step 1: Send a GET request to fetch the HTML content of a webpage
url = "https://example.com"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract specific information
# Example 1: Extract the title of the webpage
title = soup.title.string
print("Page Title:", title)

# Example 2: Find all links on the webpage
links = soup.find_all('a')
print("\nAll Links on the Page:")
for link in links:
    href = link.get('href')
    print(href)

# Example 3: Extract specific elements by class name
elements = soup.find_all('div', class_='example-class')
print("\nExtracted Elements:")
for element in elements:
    print(element.text)
