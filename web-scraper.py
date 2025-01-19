import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.wayup.com/member/jobs-listing"
# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all("h1")

    # Print the titles
    for title in titles:
        print(title.get_text())
    print(soup.contents)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
