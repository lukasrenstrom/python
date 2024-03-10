import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.hemnet.se/bostader?location_ids%5B%5D=17860"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
  
    # Find all <a> tags on the page
    a_tags = soup.find_all('a')

    # Save the text content of each <a> tag to a file
    with open('all_links.txt', 'w', encoding='utf-8') as f:
        for a_tag in a_tags:
            f.write(a_tag.text.strip() + '\n')
else:
    print("Failed to retrieve webpage")


print(response.content)
